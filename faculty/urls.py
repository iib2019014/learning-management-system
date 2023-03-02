from django.urls import path

from .views import (
    renderFacultyRegistrationView,
    renderFacultyLoginView,
)

urlpatterns = [
    path('register/', renderFacultyRegistrationView, name='faculty-register'),
    path('login/', renderFacultyLoginView, name='faculty-login'),
]