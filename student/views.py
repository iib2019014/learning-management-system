from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register
from django.contrib import messages


from .models import (
    Student,
)

from personal.models import (
    StudentRecord,
)

from .forms import (
    StudentForm
)

APPNAME = 'student'

# Create your views here.


def renderStudentRegistrationView(request) :

    context = {}

    if request.method == 'POST' :
        studentRegisterForm = StudentForm(request.POST)

        if studentRegisterForm.is_valid() :

            rollno = request.POST['rollno']

            
            try :
                record = StudentRecord.objects.get(rollno=rollno)
            except StudentRecord.DoesNotExist :
                messages.error(request, 'StudentRecord with this email does not exist!')
                return redirect('student-register')
            
            print(f'record is {record}')
            
            if record.get_student() :
                messages.error(request, 'An account with this email already exists!')
                return redirect('student-register')

            user = User.objects.create_user(
                email=record.email,
                username=request.POST['username'],
                password=request.POST['password1'],
            )

            user.groups.add(Group.objects.get(name='student'))

            student = Student.objects.create(
                user=user,
                record=record,
            )

            messages.success(request, 'Account created successfully!')

            return redirect('home')

        messages.error(request, studentRegisterForm.errors)


    studentRegisterForm = StudentForm()
    context['studentRegisterForm'] = studentRegisterForm

    return render(request, APPNAME + '/register.html', context)



def renderStudentLoginView(request) :

    context = {}

    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None :

            print("user present")

            # check if the user is a student

            if isStudent(user) :
                login(request, user)
                print("logged in")

                return redirect('student-courses')

        messages.error(request, 'Invalid Credentials!')

    return render(request, APPNAME + '/login.html', context)



def renderCoursesView(request) :
    context = {}

    return render(request, APPNAME + '/courses.html', context)














@register.filter
def isStudent(user) :
    print(user)
    if user.groups.exists() :
        print(user.groups.all())
        if user.groups.all()[0].name == 'student' :
            print(f'{user} is student')
            return True
    return False