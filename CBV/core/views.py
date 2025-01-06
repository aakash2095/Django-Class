from django.shortcuts import render

# Create your views here.


def fbv(request):
    return render(request,'core/fbv.html')