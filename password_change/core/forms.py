from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
    



class signupform(UserCreationForm):
    password2=forms.CharField(label="confirm Password",widget=forms.PasswordInput)

    class Meta():
        model=User
        fields=['username','first_name','last_name','email']


    
