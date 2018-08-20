from django.shortcuts import render, redirect
from proofs.models import *
from .forms import MajorSubmissionForm
from django.urls import reverse
from comments.forms import CommentForm
from comments.models import Comment

def home(request):
	concobj = []
	conclusions = Proof.objects.all()
	for obj in conclusions:
		concobj.insert(0, obj.conclusion)
	return render(request, 'home.html', {
		'title': 'Tümden Gelim',
		'conclusions': concobj,
	})

def about(request):
	return render(request, 'about.html')

def proposition_detail(request, id):
	proofs = Proposition.objects.get(id=id).conclusion.all()[0]
	conclusion = proofs.conclusion
	major = proofs.major
	minor = proofs.minor
	form = CommentForm()
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.user = request.user
			comment.modelObject = proofs
			comment.save()
	Comments = Comment.objects.filter(modelObject=proofs)
	return render(request, 'proposition_detail.html', {
		'proof': proofs,
		'major': major,
		'minor': minor,
		'conclusion': conclusion,
		'title': 'Önerme',
		'form': form,
		'Comments': Comments,
	})


def submit(request):
	form = MajorSubmissionForm()

	if request.method == "POST":
		form = MajorSubmissionForm(request.POST)
		if form.is_valid():
			major_type = get_proposition_type(form.cleaned_data['is_universal_major'], form.cleaned_data['is_affirmative_major'])
			minor_type = get_proposition_type(form.cleaned_data['is_universal_minor'], form.cleaned_data['is_affirmative_minor'])
			conclusion_type = get_proposition_type(form.cleaned_data['is_universal_conclusion'], form.cleaned_data['is_affirmative_conclusion'])
			type_as_string = conclusion_name(major_type, minor_type, conclusion_type)
			error = ""
			if type_as_string == 'NONE':
				error = error + "Invalid arg form: \"None\", "
			if not form.cleaned_data['subject_major'] or not form.cleaned_data['predicate_major'] or not form.cleaned_data['subject_minor'] or not form.cleaned_data['predicate_minor'] or not form.cleaned_data['subject_conclusion'] or not form.cleaned_data['predicate_conclusion']:
				error = error + "Please fill in the required fields."
			if error:
				return render(request ,"submit.html", {
						'form': form,
						'error': error
						})
			major = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_major'],
				subject=form.cleaned_data['subject_major'],
				is_affirmative=form.cleaned_data['is_affirmative_major'],
				predicate=form.cleaned_data['predicate_major'],
				user=request.user,
			)
			minor = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_minor'],
				subject=form.cleaned_data['subject_minor'],
				is_affirmative=form.cleaned_data['is_affirmative_minor'],
				predicate=form.cleaned_data['predicate_minor'],
				user=request.user,
			)
			conclusion = Proposition.objects.create(
				is_universal=form.cleaned_data['is_universal_conclusion'],
				subject=form.cleaned_data['subject_conclusion'],
				is_affirmative=form.cleaned_data['is_affirmative_conclusion'],
				predicate=form.cleaned_data['predicate_conclusion'],
				user=request.user,
			)
			major.save()
			minor.save()
			conclusion.save()
			Proof.objects.create(
				major=major,
				minor=minor,
				conclusion=conclusion,
				form_type=type_as_string
			)
			return redirect(reverse("proposition_detail", args=[conclusion.id]))

	return render(request ,"submit.html", {'form': form})

def get_proposition_type(universal, affirmative):
	if universal == 'True' and affirmative == 'True':
		return "A"
	elif universal == 'True' and affirmative == 'False':
		return "I"
	elif universal == 'False' and affirmative == 'True':
		return "E"
	else:
		return "O"

def conclusion_name(major, minor, conclusion):
	if major == "A" and minor == "A" and conclusion == "A" :
		return "Barbara"
	elif major == "E" and minor == "A" and conclusion == "E":
		return "Cesare"
	elif major == "A" and minor == "I" and conclusion == "I":
		return "Datisi"
	elif major == "E" and minor == "I" and conclusion == "O":
		return "Ferison"
	elif major == "A" and minor == "E" and conclusion == "O":
		return "Camestros"
	elif major == "A" and minor == "O" and conclusion == "O":
		return "Baroco"
	elif major == "O" and minor == "A" and conclusion == "O":
		return "Bocardo"
	elif major == "E" and minor == "A" and conclusion == "O":
		return "Celaront"
	elif major == "A" and minor == "E" and conclusion == "E":
		return "Calemes"
	elif major == "I" and minor == "A" and conclusion == "I":
		return "Disamis"
	else:
		return "NONE"