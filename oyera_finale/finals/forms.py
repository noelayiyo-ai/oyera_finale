from django import forms

class SignInForm(forms.Form):
    first_name = forms.CharField(max_length = 20, widget=forms.TextInput(attrs={"placeholder":"Enter your first name"}))
    surname = forms.CharField(max_length= 30, widget= forms.TextInput(attrs={"placeholder":"Enter your surname"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder":"example@gmail.com"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder": "Password"})) 

