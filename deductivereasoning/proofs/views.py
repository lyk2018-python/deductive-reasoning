from django.shortcuts import render
from proofs.models import Proposition, Proof
from .forms import MajorSubmissionForm 

# Create your views here.
def home(request):
	concobj = []
	conclusions = Proof.objects.all()
	for obj in conclusions:
		concobj.append(obj.conclusion)
	return render(request, 'home.html', {
		'title': 'Tümden Gelim',
		'conclusions': concobj,
	})

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
		form = SubmissionForm(request.POST)

	return render(request, 'submit.html', {'form': form})

def about(request):
	return render(request, 'about.html')