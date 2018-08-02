from django.shortcuts import render, redirect
from proofs.models import Proposition, Proof
from .forms import MajorSubmissionForm
from .typeChecker import *
from django.urls import reverse


def home(request):
	concobj = []
	conclusions = Proof.objects.all()
	for obj in conclusions:
		concobj.append(obj.conclusion)
	return render(request, 'home.html', {
		'title': 'Tümden Gelim',
		'conclusions': concobj,
	})

def about(request):
	return render(request, 'about.html')

def submit(request):
	form = MajorSubmissionForm()

def proposition_detail(request, id):
	proofs = Proposition.objects.get(id=id).conclusion.all()[0]
	conclusion = proofs.conclusion
	major = proofs.major
	minor = proofs.minor
	return render(request, 'proposition_detail.html', {
		'major': major,
		'minor': minor,
		'conclusion': conclusion,
		'title': 'Önerme',
	})

def submit(request):
	form = MajorSubmissionForm()

	if request.method == "POST":
		form = MajorSubmissionForm(request.POST)

		if form.is_valid():
			major = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_major'],
				subject=form.cleaned_data['subject_major'],
				is_affirmative=form.cleaned_data['is_affirmative_major'],
				predicate=form.cleaned_data['predicate_major'],
			)
			setPropositionType(major)
			minor = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_minor'],
				subject=form.cleaned_data['subject_minor'],
				is_affirmative=form.cleaned_data['is_affirmative_minor'],
				predicate=form.cleaned_data['predicate_minor'],
			)
			setPropositionType(minor)
			conclusion = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_conclusion'],
				subject=form.cleaned_data['subject_conclusion'],
				is_affirmative=form.cleaned_data['is_affirmative_conclusion'],
				predicate=form.cleaned_data['predicate_conclusion'],
			)
			setConclusionType(major,minor,conclusion)
			major.save()
			minor.save()
			conclusion.save()
			Proof.objects.create(
				major=major,
				minor=minor,
				conclusion=conclusion
			)
			return redirect(reverse("proposition_detail", args=[conclusion.id]))
return render(request ,"submit.html", {'form': form})