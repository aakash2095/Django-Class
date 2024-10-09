from django import forms

class MarvelForm(forms.Form):
    name=forms.CharField(error_messages={'required':'Please Enter your Name'})
    email=forms.EmailField()

    def clean(self):
        cleaned_data = super().clean()

        validate_name = cleaned_data['name']

        validate_email = cleaned_data['email']

        if len(validate_name)>5:
            raise forms.ValidationError('Enter the Name Less than 5 words')
        
        if len(validate_email)<8:
            raise forms.ValidationError('Enter the email ')

