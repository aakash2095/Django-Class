from django.shortcuts import render, redirect ,get_object_or_404
from .forms import Registerform, Authenticateform , userchange ,AdminProfileForm , changepasswordform
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib import messages
from . models import new_arrival,CartUpperwear

def index(request):
    return render(request, 'core/index.html')

####################  REGISTER AND LOGIN #########################

def register(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            rf = Registerform(request.POST)
            if rf.is_valid():
                rf.save()
                messages.success(request, 'Registration Successful')
                return redirect('login')
        else:
            rf = Registerform()
        return render(request, 'core/register.html', {'rf': rf})
    else:
        return redirect('profile')

def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            rf = Authenticateform(request, request.POST)
            if rf.is_valid():
                name = rf.cleaned_data['username']
                pas = rf.cleaned_data['password']
                user = authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)  
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid username or password')
        else:
            rf = Authenticateform()
        return render(request, 'core/login.html', {'rf': rf})
    else:
        return redirect('profile')

def log_out(request):
    logout(request)
    return redirect('register')



def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.user.is_superuser:
                rf = AdminProfileForm(request.POST, instance=request.user)
            else:
                rf = userchange(request.POST, instance=request.user)

            if rf.is_valid():
                rf.save()
                messages.success(request, 'Profile Updated Successfully !!')
        else:
            if request.user.is_superuser:
                rf = AdminProfileForm(instance=request.user)
            else:
                rf = userchange(instance=request.user)
                
        return render(request, 'core/profile.html', {'name': request.user, 'rf': rf})
    else:
        return redirect('login')


def changepassword(request):                                                     
    if request.user.is_authenticated:                              
        if request.method == 'POST':                               
            rf =changepasswordform(request.user,request.POST)
            if rf.is_valid():
                rf.save()
                update_session_auth_hash(request,rf.user)
                return redirect('profile')
        else:
            rf = changepasswordform(request.user)
        return render(request,'core/changepassword.html',{'rf':rf})
    else:
        return redirect('login')

    
####################  FETCHING IMAGE THROUGH DATABASE AND REDIRECT TO DETAILS PAGE #########################

def trending(request):
    return render(request,'core/trending.html')

def newarrival(request):
    rf=new_arrival.objects.filter(category='NEWARRIVAL')
    return render (request,'core/newarrival.html',{'rf':rf})

def shirt(request):
    rf=new_arrival.objects.filter(category='SHIRTS')
    return render (request,'core/shirt.html',{'rf':rf})


def Tshirt(request):
    rf=new_arrival.objects.filter(category='T_SHIRTS')
    return render (request,'core/Tshirt.html',{'rf':rf})
    

def bigcard(request,id):
    rf=new_arrival.objects.get(pk=id)
    return render(request,'core/bigcard.html',{'rf':rf})






####################  ADD TO CART #########################




def add_to_cart(request, id):
    na = new_arrival.objects.get(pk=id)  
    user = request.user
    CartUpperwear(user=user, product=na).save()
    messages.success(request,'ADDED TO CART!!')
    return redirect('bigcard', id)


def showcart(request):
    ca=CartUpperwear.objects.filter(user=request.user)
    return render (request,'core/showcart.html',{'ca':ca})

def delete_cart(request, id):
    ca = CartUpperwear.objects.get(pk=id) 
    ca.delete()
    return redirect('showcart') 


def add_item(request,id):
    product =get_object_or_404(CartUpperwear,pk=id)
    product.quantity +=1
    product.save()
    return redirect('showcart')

def delete_item(request,id):
    product=get_object_or_404(CartUpperwear,pk=id)
    if product.quantity>1:
        product.quantity -=1
        product.save()
    return redirect('showcart')

