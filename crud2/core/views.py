from django.shortcuts import render,redirect
from .forms import MarvelForm
from .models import Marvel


# Create your views here.

def base(request):
    if request.method == 'POST':
        mf= MarvelForm (request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('base')
    else:
        mf=MarvelForm()
        mm=Marvel.objects.all
        return render(request,'core/base.html',{'mf':mf,'marvel':mm})

def delete(request,id):
    if request.method == 'POST':
        mm=Marvel.objects.get(pk=id)
        mm.delete()
        return redirect('base')
    

def update(request,id):
    if request.method == 'POST':
        mm=Marvel.objects.get(pk=id)
        mf=MarvelForm(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
    else:
        mm=Marvel.objects.get(pk=id)
        mf=MarvelForm(instance=mm)
        return render (request,'core/update.html',{'mf':mf})

       