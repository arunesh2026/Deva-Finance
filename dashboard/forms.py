from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm




class SignUpForm(UserCreationForm):
    #ERROR :        change later - error message
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}), label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control mb-3"}), label="Confirm Password")
    
    class Meta:
        model = User
        fields = ["username", "email"]
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control mb-3"}),
            "email": forms.EmailInput(attrs={"class": "form-control mb-3"}),
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control mb-3'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control mb-3'}))