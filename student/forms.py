from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Student,
)


class StudentForm(UserCreationForm) :

    rollno = forms.CharField(max_length=255, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='password', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='password', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta :
        model = User
        fields = ('rollno', 'username', 'password1', 'password2')