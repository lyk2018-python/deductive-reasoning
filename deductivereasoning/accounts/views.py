from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib import messages


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'accounts/profile.html', {
        'user': user,
    })

def dashboard(request):
    return render(request, 'accounts/dashboard.html', {'title': 'Profile Page'})
