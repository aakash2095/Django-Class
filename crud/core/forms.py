from django import forms
from .models import Marvel

class Marvelform(forms.ModelForm):


    class Meta:
        model=Marvel
        fields='__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control col-auto'}),
            'Email':forms.TextInput(attrs={'class':'form-control'})          
            
        }