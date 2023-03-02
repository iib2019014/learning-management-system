from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import (
    Student,
)


class StudentForm(UserCreationForm) :

    rollno = forms.CharField(max_length=255, required=True)

    class Meta :
        model = User
        fields = ('rollno', 'username', 'password1', 'password2')