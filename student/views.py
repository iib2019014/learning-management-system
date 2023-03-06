from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register
from django.contrib import messages


from .models import (
    Student,
)

from personal.models import (
    Course,
    StudentRecord,

    MIN_CREDITS,
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

        # print(username, password)

        user = authenticate(request, username=username, password=password)

        if user is not None :

            # print("user present")

            # check if the user is a student

            if isStudent(user) :
                login(request, user)
                # print("logged in")

                return redirect('student-courses')

        messages.error(request, 'Invalid Credentials!')

    return render(request, APPNAME + '/login.html', context)



def renderCoursesView(request) :
    context = {}

    # student = request.user.student

    # courses = student.courses.all()

    # context['courses'] = courses

    return render(request, APPNAME + '/courses.html', context)



def renderAvailableCoursesView(request) :
    context = {}


    if request.method == 'POST' :
        checked_ids = request.POST.getlist('available_courses')
        print(checked_ids)


        checked_courses = []
        credits = 0

        for id in checked_ids :
            course = Course.objects.get(id=id)
            checked_courses.append(course)

            credits += course.credits

        if credits < MIN_CREDITS :
            messages.warning(request, f'You need to select courses for at least {MIN_CREDITS} credits!')

            return redirect('available-courses')
        
        for course in checked_courses :
            student = request.user.student
            student.courses.add(course)
        student.save()

        messages.success(request, 'Successfully added courses!')

        return redirect('home')



    courses = Course.objects.all()

    context['courses'] = courses

    return render(request, APPNAME + '/enrollment.html', context)











@register.filter
def isStudent(user) :
    # print(user)
    if user.groups.exists() :
        # print(user.groups.all())
        if user.groups.all()[0].name == 'student' :
            # print(f'{user} is student')
            return True
    return False