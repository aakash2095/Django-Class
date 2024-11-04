from django.shortcuts import render, redirect
from .forms import Registerform, Authenticateform , userchange ,AdminProfileForm , changepasswordform
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
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
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                rf = AdminProfileForm(request.POST, instance=request.user)
            else:
                rf = userchange(request.POST, instance=request.user)

            if rf.is_valid():
                rf.save()
                messages.success(request, 'Profile Updated Successfully !!')
        else:
            if request.user.is_superuser:
                rf = AdminProfileForm(instance=request.user)
            else:
                rf = userchange(instance=request.user)
                
        return render(request, 'core/profile.html', {'name': request.user, 'rf': rf})
    else:
        return redirect('login')


def changepassword(request):                                                     
    if request.user.is_authenticated:                              
        if request.method == 'POST':                               
            rf =changepasswordform(request.user,request.POST)
            if rf.is_valid():
                rf.save()
                update_session_auth_hash(request,rf.user)
                return redirect('profile')
        else:
            rf = changepasswordform(request.user)
        return render(request,'core/changepassword.html',{'rf':rf})
    else:
        return redirect('login')

    


def trending(request):
    return render(request,'core/trending.html')

def newarrival(request):
    return render (request,'core/newarrival.html')