from django.shortcuts import render
from proofs.models import Proposition, Proof

# Create your views here.
def home(request):
	propositions = Proposition.objects.all()
	proofs = Proof.objects.all()
	return render(request, 'home.html', {
		'title': 'Tümden Gelim',
		'propositions': propositions,
		'proofs': proofs,
	})