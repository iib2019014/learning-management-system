from django.urls import path

from .views import (
    renderStudentRegistrationView,
    renderStudentLoginView,
)

urlpatterns = [
    path('register/', renderStudentRegistrationView, name='student-register'),
    path('login/', renderStudentLoginView, name='student-login'),
]