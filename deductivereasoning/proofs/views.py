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
	return render(request, 'submit.html', {'form': form})

def about(request):
	return render(request, 'about.html')