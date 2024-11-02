from django.shortcuts import render, redirect
from .forms import Registerform, Authenticateform
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'core/index.html')

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            rf = Registerform(request.POST)
            if rf.is_valid():
                rf.save()
                messages.success(request, 'Registration Successful')
                return redirect('login')
        else:
            rf = Registerform()
        return render(request, 'core/register.html', {'rf': rf})
    else:
        return redirect('profile')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            rf = Authenticateform(request, request.POST)
            if rf.is_valid():
                name = rf.cleaned_data['username']
                pas = rf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)  
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password')
        else:
            rf = Authenticateform()
        return render(request, 'core/login.html', {'rf': rf})
    else:
        return redirect('profile')

def log_out(request):
    logout(request)
    return redirect('register')

def profile(request):
    return render(request, 'core/profile.html')


def trending(request):
    return render(request,'core/trending.html')

def newarrival(request):
    return render (request,'core/newarrival.html')