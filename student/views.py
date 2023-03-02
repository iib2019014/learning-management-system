from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register


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
        print("post")
        studentRegisterForm = StudentForm(request.POST)

        if studentRegisterForm.is_valid() :

            print("valid")
            
            rollno = request.POST['rollno']

            record = StudentRecord.objects.filter(rollno__iexact=rollno).first()


            if record :

                print("record found")

                if not record.get_student() :

                    print("not registered")

                    # create a user
                    user = User.objects.create_user(
                        email=record.email,
                        username=request.POST['username'],
                        password=request.POST['password1']
                    )

                    # add the user to 'student' group
                    user.groups.add(Group.objects.get(name='student'))
                    print("group added")

                    # create student with this user,
                    student = Student.objects.create(
                        user=user,
                        record = record,
                    )

                    print(student, " created")

                    return redirect('home')


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

                return redirect('home')

    return render(request, APPNAME + '/login.html', context)



@register.filter
def isStudent(user) :
    print(user)
    if user.groups.exists() :
        print(user.groups.all())
        if user.groups.all()[0].name == 'student' :
            print(f'{user} is student')
            return True
    return False