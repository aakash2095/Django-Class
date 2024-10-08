from django import forms


class Marvelform(forms.Form):
    name=forms.CharField()