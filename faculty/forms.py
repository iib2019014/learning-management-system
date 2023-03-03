from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Faculty,
)



class FacultyForm(UserCreationForm) :
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}),
    )

    class Meta :
        model = User
        fields = ('email', 'username', 'password1', 'password2')