from django.shortcuts import render,redirect
from . forms import Registerform
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def register(request):
    if request.method=="POST":
        rf=Registerform(request.POST)
        if rf.is_valid():
            rf.save()
            messages.success(request,'Registration Succesfull')
            return redirect('register')
    else:
        rf=Registerform()
        return render(request,'core/register.html',{'rf':rf})

