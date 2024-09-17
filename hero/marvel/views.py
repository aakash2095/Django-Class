from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def marvel (request):
    return HttpResponse('i am spiderman')