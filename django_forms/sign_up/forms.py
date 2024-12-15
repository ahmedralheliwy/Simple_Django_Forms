from django import forms
from .models import Sign_Up

class Sign_UpForm(forms.ModelForm):
    class Meta:
        model=Sign_Up
        fields='__all__'