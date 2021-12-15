from django import forms
from django.core.validators import ValidationError
from django.contrib.auth.models import User
from .models import UserStory


class LoginForm(forms.Form):
    """Form for login"""
    login = forms.CharField(label="Login")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


def login_not_taken(login):
    """Validates login is it taken."""
    if User.objects.filter(username=login):
        raise ValidationError('Podany login jest zajęty')


class AddUserForm(forms.Form):
    """Creates a form to add a new user to our app"""
    login = forms.CharField(label="Login", max_length=32, validators=[login_not_taken])
    password = forms.CharField(label="Hasło", widget=forms.PasswordInput, max_length=32)
    password2 = forms.CharField(label="Powtórz hasło", widget=forms.PasswordInput, max_length=32)
    first_name = forms.CharField(label="Imię", max_length=64)
    last_name = forms.CharField(label="Nazwisko", max_length=64)
    email = forms.EmailField(label="e-mail")

    def clean(self):
        """Checks if password1 and to password2 are the same."""
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            raise ValidationError("Hasła nie są takie same")
        return cleaned_data


class UserStoryForm(forms.ModelForm):
    """Form to add short work from users"""
    class Meta:
        model = UserStory
        fields = ['tittle', 'story']



