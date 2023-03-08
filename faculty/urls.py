from django.urls import path

from .views import (
    renderFacultyHomeView,
    renderFacultyRegistrationView,
    renderFacultyLoginView,
    renderCourseView,
)

urlpatterns = [
    path('', renderFacultyHomeView, name='faculty-home'),
    path('register/', renderFacultyRegistrationView, name='faculty-register'),
    path('login/', renderFacultyLoginView, name='faculty-login'),
    path('course/<str:course_id>', renderCourseView, name='faculty-course'),
]