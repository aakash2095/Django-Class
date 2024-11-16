from django.shortcuts import render, redirect ,get_object_or_404
from .forms import Registerform, Authenticateform , userchange ,AdminProfileForm , changepasswordform , Userform
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash
from django.contrib import messages
from . models import new_arrival,CartUpperwear,Userdetails,Order



from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse


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

########################## ADDRESS PAGE #########################

def address(request):
    if request.method == 'POST':
        rf=Userform(request.POST)
        if rf.is_valid():
            user=request.user
            name= rf.cleaned_data['name']
            address= rf.cleaned_data['address']
            city= rf.cleaned_data['city']
            state= rf.cleaned_data['state']
            pincode= rf.cleaned_data['pincode']
            Userdetails(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
            return redirect('showaddress')
    else:
        rf =Userform()
        address = Userdetails.objects.filter(user=request.user)
    return render(request,'core/address.html',{'rf':rf,'address':address})


def delete_address(request,id):
    if request.method == 'POST':
        rf = Userdetails.objects.get(pk=id)
        rf.delete()
    return redirect('showaddress')

def showaddress(request):
    address = Userdetails.objects.filter(user=request.user)
    return render(request,'core/showaddress.html',{'address':address})

###################################  CHECKOUT PAGE ####################################

def checkout(request):
    ca=CartUpperwear.objects.filter(user=request.user)
    total=0
    Delivery_charge = 149 
    for c in ca :
        total+=(c.product.discounted_price*c.quantity)
        final_price = total+Delivery_charge
    address=Userdetails.objects.filter(user=request.user)
    return render(request, 'core/checkout.html', {'ca': ca,'total':total,'final_price':final_price,'address':address})
    


def payment(request):
    if request.method == 'POST':
        selected_address_id= request.POST.get('selected_address')
    ca=CartUpperwear.objects.filter(user=request.user)
    total=0
    Delivery_charge = 149 
    for c in ca :
        total+=(c.product.discounted_price*c.quantity)
        final_price = total+Delivery_charge
    address=Userdetails.objects.filter(user=request.user)
    #============== Paypal Code =====================
   
    host = request.get_host()   # Will fecth the domain site is currently hosted on.
   
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,   #This is typically the email address associated with the PayPal account that will receive the payment.
        'amount': final_price,    #: The amount of money to be charged for the transaction. 
        'item_name': 'Pet',       # Describes the item being purchased.
        'invoice': uuid.uuid4(),  #A unique identifier for the invoice. It uses uuid.uuid4() to generate a random UUID.
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",         #The URL where PayPal will send Instant Payment Notifications (IPN) to notify the merchant about payment-related events
        'return_url': f"http://{host}{reverse('paymentsuccess',args=[selected_address_id])}",     #The URL where the customer will be redirected after a successful payment. 
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",      #The URL where the customer will be redirected if they choose to cancel the payment. 
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

        #=============== Paypal Code  End =====================

    return render(request,'core/payment.html',{'paypal':paypal_payment})


def payment_success(request, selected_address_id):
    user = request.user
    address_data = Userdetails.objects.get(pk=selected_address_id)
    cart = CartUpperwear.objects.filter(user=request.user)
    
    for cart in cart:
        Order(
            user=user,
            customer=address_data,
            quantity=cart.quantity,
            cloth=cart.product).save()
        cart.delete() 
    
    return render(request, 'core/payment_success.html')



def payment_failed(request):
    return render(request,'core/payment_failed.html')

def order(request):
    ord=Order.objects.filter(user=request.user)
    return render (request,'core/order.html',{'ord':ord})
