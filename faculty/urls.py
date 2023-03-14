from django.urls import path

from .views import (
    renderFacultyHomeView,
    renderFacultyRegistrationView,
    renderFacultyLoginView,
    renderCourseView,
    renderClassPeopleView,
    
    renderMaterialsView,
    renderCreateMaterialView,
    renderEditMaterialView,
    renderDeleteMaterialView,

    renderAssignmentsView,
    renderCreateAssignmentView,
    renderEditAssignmentView,
    renderDeleteAssignmentView,

    renderAttendancesView,
    renderCreateAttendanceView,
)

urlpatterns = [
    path('', renderFacultyHomeView, name='faculty-home'),
    path('register/', renderFacultyRegistrationView, name='faculty-register'),
    path('login/', renderFacultyLoginView, name='faculty-login'),

    
    path('course/<str:course_id>', renderCourseView, name='faculty-course'),
    path('class/<str:course_id>', renderClassPeopleView, name='people'),


    path('materials/<str:course_id>', renderMaterialsView, name='faculty-materials'),
    path('create-material/<str:course_id>', renderCreateMaterialView, name='create-material'),
    path('edit-material/<str:material_id>', renderEditMaterialView, name='edit-material'),
    path('delete-material/<str:material_id>', renderDeleteMaterialView, name='delete-material'),


    path('assignments/<str:course_id>', renderAssignmentsView, name='faculty-assignments'),
    path('create-assignment/<str:course_id>', renderCreateAssignmentView, name='create-assignment'),
    path('edit-assignment/<str:assignment_id>', renderEditAssignmentView, name='edit-assignment'),
    path('delete-assignment/<str:assignment_id>', renderDeleteAssignmentView, name='delete-assignment'),


    path('attendances/<str:course_id>', renderAttendancesView, name='faculty-attendances'),
    path('create-attendance/<str:course_id>', renderCreateAttendanceView, name='create-attendance'),

]