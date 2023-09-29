from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=254)
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'confirm_password')