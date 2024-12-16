from django import forms
from .models import Sign_Up

class Sign_UpForm(forms.ModelForm):
    class Meta:
        model=Sign_Up
        fields='__all__'

        widgets={
           'username':forms.TextInput(attrs={'class':'form-control'}), 
           'email':forms.EmailInput(attrs={'class':'form-control'}), 
           'password':forms.PasswordInput(attrs={'class':'form-control'}), 
        }