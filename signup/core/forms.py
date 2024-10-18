from django import forms
from django.contrib.auth.forms import UserCreationForm


class signupform(UserCreationForm):
    fields='__all__'



    
