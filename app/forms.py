from app.models import *
from django import forms

class UserForm(forms.ModelForm):
    class Meta():
        model=User
        model=User
        fields=['username','email','password']
        widgets={'password':forms.PasswordInput()}

class countryForm(forms.ModelForm):
    class Meta():
        model = country
        fields = '__all__'