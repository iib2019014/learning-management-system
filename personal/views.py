from django.shortcuts import render, redirect
from django.contrib.auth import logout


from .models import (
    Course,
)



APPNAME = 'personal'

# Create your views here.


def renderHomeView(request) :
    context = {}

    print("in home view")
    return render(request, APPNAME + '/home.html', context)


def renderLogoutView(request) :
    context = {}

    if request.user.is_authenticated :
        logout(request)

    return redirect('home')
    # return render(request, APPNAME + '/home.html', context)



def renderAvailableCoursesView(request) :
    context = {}

    courses = Course.objects.all()

    context['courses'] = courses

    return render(request, APPNAME + '/enrollment.html', context)