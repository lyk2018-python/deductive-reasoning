from django.shortcuts import render
from proofs.models import Proposition, Proof
from .forms import MajorSubmissionForm

# Create your views here.
def home(request):
	propositions = Proposition.objects.all()
	proofs = Proof.objects.all()
	return render(request, 'home.html', {
		'title': 'Tümden Gelim',
		'propositions': propositions,
		'proofs': proofs,
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
			minor = Proposition.objects.create(
			is_universal=form.cleaned_data['is_universal_minor'],
			subject=form.cleaned_data['subject_minor'],
			is_affirmative=form.cleaned_data['is_affirmative_minor'],
			predicate=form.cleaned_data['predicate_minor'],
			)
			conclusion = Proposition.objects.create(
			is_universal=form.cleaned_data['is_universal_conclusion'],
			subject=form.cleaned_data['subject_conclusion'],
			is_affirmative=form.cleaned_data['is_affirmative_conclusion'],
			predicate=form.cleaned_data['predicate_conclusion'],
			)
			#proof_major = Proof.objects.create(major)
			#proof_minor = Proof.objects.create(minor)
			#proof_conclusion = Proof.objects.create(conclusion)



	return render(request ,"submit.html", {'form': form})
