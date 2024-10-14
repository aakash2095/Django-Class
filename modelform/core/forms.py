from django import forms
from . models import Marvel

#class MarvelForm(forms.Form):
    # name = forms.CharField(label='Heroic Name',label_suffix=' - ',disabled=False,required=False,initial='Captain')
    # name=forms.CharField(label='Heroic Name',widget=forms.TextInput(attrs={'class':'hn','placeholder':'Enter the name of hero'}))
    #name =forms.CharField()
    #heroic_name=forms.CharField()
    

class MarvelForm(forms.ModelForm):

    class Meta:
        model = Marvel
        fields = ['name','heroic_name']
        labels = {'name':'Full Name'}

        error_messages={
            'Full Name':{'required':'Enter Your Name'},
            'heroic_name':{'required':'Enter Heroic name'}
        }

        widgets = {
            'heroic_name':forms.TextInput(attrs={'class':'form-control'}),
            'Full Name': forms.PasswordInput()
        }
