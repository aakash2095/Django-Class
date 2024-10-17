from django.shortcuts import render,redirect
from .models import Marvel
from .forms import Marvelform


# Create your views here.

def base(request):
    if request.method == 'POST':
        mf=Marvelform(request.POST)
        if mf.is_valid():
            mf.save()
        return redirect('base')
    else:
        mf =Marvelform()
        mm = Marvel.objects.all()
        return render(request,'core/base.html',{'mf':mf,'marvel':mm})