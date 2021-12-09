from django import forms
from django.core.validators import validate_email


class LoginForm(forms.Form):
    """Form for login"""
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)