from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register
from django.contrib import messages

from .models import (
    Faculty,
)

from student.views import (
    isStudent,
)

from personal.models import (
    Course,
    FacultyRecord,
)

from .forms import (
    FacultyForm,
)

from course.models import (
    Material,
)

from course.forms import (
    MaterialForm,
)


APPNAME = 'faculty'


# Create your views here.

def renderFacultyHomeView(request) :
    context = {}
    
    if request.user.is_authenticated :
        faculty = request.user.faculty

        # get the courses of a faculty (it is foreign key relation),
        courses = faculty.course_set.all()

        context['courses'] = courses

        return render(request, APPNAME + '/home.html', context)
    
    return redirect('home')

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
                messages.error(request, 'FacultyRecord with this email does not exist!')
                return redirect('faculty-register')
            
            print(f'record is {record}')

            if record.get_faculty() :
                messages.error(request, 'An account with this email already exists!')
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

            messages.success(request, 'Account created successfully!')

            return redirect('home')
        
        # print(facultyRegisterForm.errors)
        messages.error(request, facultyRegisterForm.errors)


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

                return redirect('faculty-home')
            
        messages.error(request, 'Invalid Credentials!')

    return render(request, APPNAME + '/login.html', context)



def renderCourseView(request, course_id) :
    context = {}

    try: 
        course = Course.objects.get(id=course_id)

    except :
        return redirect('faculty-home')


    # print(f'{course}')
    context['course'] = course

    return render(request, APPNAME + '/course.html', context)


def renderMaterialsView(request, course_id) :
    if not request.user.is_authenticated :
        return redirect('home')
    
    context = {}
    course = None

    try :
        course = Course.objects.get(id=course_id)
        context['course'] = course

    except Course.DoesNotExist :
        return redirect('home')
    
    materials = course.material_set.all()

    print(f'{materials}')

    context['materials'] = materials


    return render(request, APPNAME + '/materials.html', context)



def renderCreateMaterialView(request, course_id) :
    if not request.user.is_authenticated or isStudent(request.user) :
        return redirect('home')
    
    context = {}
    course = None


    try :
        course = Course.objects.get(id=course_id)
        context['course'] = course

    except Course.DoesNotExist :
        return redirect('faculty-home')

    if request.method == 'POST' :
        materialForm = MaterialForm(request.POST)

        if materialForm.is_valid() :
            
            Material.objects.create(
                name=request.POST.get('name'),
                course=course,
                material_type=request.POST.get('material_type'),
                link=request.POST.get('link'),
                file=request.POST.get('file')
            )

            messages.success(request, 'Material added successfully!')

            return redirect('faculty-materials', course_id=course_id)
        


    materialForm = MaterialForm()
    context['materialForm'] = materialForm

    return render(request, APPNAME + '/createMaterial.html', context)





@register.filter
def isFaculty(user) :
    print(user)
    if user.groups.exists() :
        print(user.groups.all())
        if user.groups.all()[0].name == 'faculty' :
            print(f'{user} is faculty')
            return True
    return False