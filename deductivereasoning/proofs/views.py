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

def proposition_detail(request, id):
	proposition = Proposition.objects.get(id=id)
	major = proposition.major.all()
	minor = proposition.minor.all()
	conclusion = proposition.conclusion.all()
	return render(request, 'proposition_detail.html', {
		'proposition': proposition,
		'major': major,
		'minor': minor,
		'conclusion': conclusion,
		'title': 'Önerme',
	})


def submit(request):
	form = MajorSubmissionForm()
	if request.method == "POST":
		form = SubmissionForm(request.POST)

	return render(request ,"submit.html", {'form': form})