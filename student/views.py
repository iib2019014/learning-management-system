from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from django.template.defaulttags import register
from django.contrib import messages

from course.models import Assignment


from .models import (
    Student,
    Submission,
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


def renderStudentHomeView(request) :
    context = {}

    if request.user.is_authenticated :
        student = request.user.student
        courses = student.courses.all()

        context['courses'] = courses

        return render(request, APPNAME + '/home.html', context)
    
    return redirect('home')


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

                return redirect('student-home')

        messages.error(request, 'Invalid Credentials!')

    return render(request, APPNAME + '/login.html', context)







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

        student.enrolled = True

        student.save()

        messages.success(request, 'Successfully added courses!')

        return redirect('home')



    courses = Course.objects.all()

    context['courses'] = courses

    return render(request, APPNAME + '/enrollment.html', context)




def renderCourseView(request, course_id) :
    context = {}

    course = None

    try :
        course = Course.objects.get(id=course_id)

    except Course.DoesNotExist :
        return redirect('student-home')
    
    print(f'{course}')
    context['course'] = course

    return render(request, APPNAME + '/course.html', context)


def renderClassPeopleView(request, course_id) :
    if not request.user.is_authenticated or not isStudent(request.user) :
        messages.error(request, 'You are not allowed to perform this operation!')
        return redirect('home')
    
    context = {}
    course = None

    try :
        course = Course.objects.get(id=course_id)
        context['course'] = course

    except Course.DoesNotExist :
        return redirect('home')
    
    classmates = course.student_set.all()
    context['classmates'] = classmates

    return render(request, APPNAME + '/people.html', context)


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



def renderAssignmentsView(request, course_id) :
    if not request.user.is_authenticated or not isStudent(request.user) :
        messages.error(request, 'You are not allowed to perform this operation!')
        return redirect('home')
    

    context = {}
    course = None

    try :
        course = Course.objects.get(id=course_id)
        context['course'] = course

    except Course.DoesNotExist :
        return redirect('home')


    assignments = course.assignment_set.all()

    print(f'{assignments}')

    context['assignments'] = assignments

    submitteds, lates = [], []


    # for each assignment, get the submission object and store the value of submitted and late
    for assignment in assignments :
        submission = Submission.objects.get(assignment=assignment, student=request.user.student)
        submitteds.append(submission.submitted)
        lates.append(submission.late)

    # the values of submitted and late can be given to template in this way or we can use the method like how we get the isStudent value
    # i.e. request.user.student|submitted


    assignments_submissions = zip(assignments, submitteds, lates)

    context['assignments_submissions'] = assignments_submissions


    return render(request, APPNAME + '/assignments.html', context)


def renderAssignmentSubmissionView(request, assignment_id) :
    if not request.user.is_authenticated or not isStudent(request.user) :
        messages.error(request, 'You are not allowed to perform this operation!')
        return redirect('home')
    
    context = {}
    assignment = None

    try :
        assignment = Assignment.objects.get(id=assignment_id)
        context['assignment'] = assignment
        course = assignment.course
        context['course'] = course

    except Assignment.DoesNotExist :
        return redirect('home')
    

    if request.method == 'POST' :
        submission = Submission.objects.get(student=request.user.student, assignment=assignment)

        submission.answer_file = request.FILES['answer_file']
        submission.submitted = True

        submission.save()

        messages.success(request, 'Assignment submitted successfully!')

        return redirect('student-assignments', course_id=course.id)

    return render(request, APPNAME + '/submitAssignment.html', context)



@register.filter
def isStudent(user) :
    # print(user)
    if user.groups.exists() :
        # print(user.groups.all())
        if user.groups.all()[0].name == 'student' :
            # print(f'{user} is student')
            return True
    return False