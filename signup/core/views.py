from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method == 'POST':
        mf =UserCreationForm(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'USER LOGGED IN SUCCESSFULLY')
    else:
        mf=UserCreationForm()
    return render(request,'core/index.html',{'mf':mf})