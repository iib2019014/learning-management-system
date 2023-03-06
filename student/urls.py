from django.urls import path

from .views import (
    renderStudentRegistrationView,
    renderStudentLoginView,
    renderCoursesView,
    renderAvailableCoursesView,
)

urlpatterns = [
    path('register/', renderStudentRegistrationView, name='student-register'),
    path('login/', renderStudentLoginView, name='student-login'),
    path('courses/', renderCoursesView, name='student-courses'),
    path('enrollment/', renderAvailableCoursesView, name='available-courses'),
]