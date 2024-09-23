from django.shortcuts import render

# Create your views here.
def spiderman (request):
    context={'superhero':{'spidy':'spiderman','bat':'batman'},'villain':['Amar','aashay','abhishek']}
    return render(request,'marvel/spiderman.html',context)