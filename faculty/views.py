from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register

from .models import (
    Faculty,
)

from personal.models import (
    FacultyRecord,
)

from .forms import (
    FacultyForm,
)


APPNAME = 'faculty'


# Create your views here.

def renderFacultyRegistrationView(request) :

    context = {}

    if request.method == 'POST' :
        facultyRegisterForm = FacultyForm(request.POST)

        if facultyRegisterForm.is_valid() :
            
            # check if a facultyrecord with the given exists,
            email = request.POST['email']

            try :
                record = FacultyRecord.objects.get(email=email)
            except FacultyRecord.DoesNotExist :
                return redirect('faculty-register')
            
            print(f'record is {record}')

            if record.get_faculty() :
                return redirect('faculty-register')
            
            user = User.objects.create_user(
                email=email,
                username=request.POST['username'],
                password=request.POST['password1'],
            )

            # add the user to faculty group
            user.groups.add(Group.objects.get(name='faculty'))

            faculty = Faculty.objects.create(
                user=user,
                record=record,
            )

            return redirect('home')

    else :
        context['facultyRegisterForm'] = FacultyForm()

    return render(request, APPNAME +  '/register.html', context)


def renderFacultyLoginView(request) :

    context = {}

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None :

            print("user present")

            # check if the user is a faculty

            if isFaculty(user) :
                login(request, user)
                print("logged in")

                return redirect('home')

    return render(request, APPNAME + '/login.html', context)



@register.filter
def isFaculty(user) :
    print(user)
    if user.groups.exists() :
        print(user.groups.all())
        if user.groups.all()[0].name == 'faculty' :
            print(f'{user} is faculty')
            return True
    return False