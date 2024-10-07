from django import forms


class Marvelform(forms.Form):
    # name = forms.CharField(label='Heroic Name',label_suffix=' - ',disabled=False,required=False,initial='Captain')
    name=forms.CharField(label='Heroic Name',widget=forms.TextInput(attrs={'class':'hn','placeholder':'Enter the name of hero'}))

    