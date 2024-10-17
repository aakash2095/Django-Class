from django.shortcuts import render,redirect
from .models import Marvel
from .forms import Marvelform
from django.contrib import messages


# Create your views here.

def base(request):
    if request.method == 'POST':
        mf=Marvelform(request.POST)
        if mf.is_valid():
            mf.save()
            messages.success(request,'USER ADDED SUCCESSFULLY')
        return redirect('base')
    else:
        mf =Marvelform()
        mm = Marvel.objects.all()
        return render(request,'core/base.html',{'mf':mf,'marvel':mm})
    

def delete(request,id):
    if request.method == 'POST':
        mm=Marvel.objects.get(pk=id)
        mm.delete()
        return redirect('base')
    
def update(request,id):
    if request.method == 'POST':
        mm=Marvel.objects.get(pk=id)
        mf = Marvelform(request.POST,instance=mm)
        if mf.is_valid():
            mf.save()
    else:
        mm=Marvel.objects.get(pk=id)
        mf= Marvelform(instance=mm)
    return render(request,'core/update.html',{'mf':mf})