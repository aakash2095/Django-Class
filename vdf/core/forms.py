from django import forms

class MarvelForm(forms.Form):
    name=forms.CharField(error_messages={'required':'Please Enter your Name'})
    email=forms.EmailField()