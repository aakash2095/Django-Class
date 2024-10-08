from django.shortcuts import render
from .forms import Marvelform

# Create your views here
 
def index (request):
    mf = Marvelform()
    return render(request,'core/index.html',{'mf':mf})