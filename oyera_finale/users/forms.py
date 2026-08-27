from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User 


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name","email", "username", "password1", "password2"]
        labels ={
            'first_name': "Enter your firstname",
            'last_name': 'Enter your lastname',
            'username': 'Shortened name version',
            'email': 'Enter your email',
            'password1': 'Enter a strong password',
            'password2': 'Confirm your password',
        }


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {
            'username': 'Enter username',
            'password': 'Enter password',
        }