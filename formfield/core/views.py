from django.shortcuts import render,redirect
from .forms import MarvelForm

def index(request):
    if request.method == 'POST':
        mf =MarvelForm(request.POST)
        if mf.is_valid():
            print('name..',mf.cleaned_data['name'])
            print('email..',mf.cleaned_data['email'])
        
        mf =MarvelForm()
        # return render(request,'core/success.html')
        # return redirect('success')
    else:
        mf= MarvelForm()
    return render(request,'core/index.html',{'mf':mf})
