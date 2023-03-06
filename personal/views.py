from django.shortcuts import render, redirect
from django.contrib.auth import logout


from .models import (
    Course,
)

from student.views import (
    isStudent,
)



APPNAME = 'personal'

# Create your views here.


def renderHomeView(request) :
    context = {}

    if request.user.is_authenticated :
        if isStudent(request.user) :
            return redirect('student-home')
        return redirect('faculty-home')

    print("in home view")
    return render(request, APPNAME + '/home.html', context)


def renderLogoutView(request) :
    context = {}

    if request.user.is_authenticated :
        logout(request)

    return redirect('home')
    # return render(request, APPNAME + '/home.html', context)