from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def spiderman(request):
    return HttpResponse('i am spiderman')

def ironman(request):
    return HttpResponse('i am ironman')

def antman(request):
    return HttpResponse('i am antman')