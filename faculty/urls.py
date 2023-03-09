from django.urls import path

from .views import (
    renderFacultyHomeView,
    renderFacultyRegistrationView,
    renderFacultyLoginView,
    renderCourseView,
    renderMaterialsView,
    renderCreateMaterialView,
)

urlpatterns = [
    path('', renderFacultyHomeView, name='faculty-home'),
    path('register/', renderFacultyRegistrationView, name='faculty-register'),
    path('login/', renderFacultyLoginView, name='faculty-login'),
    path('course/<str:course_id>', renderCourseView, name='faculty-course'),
    path('materials/<str:course_id>', renderMaterialsView, name='faculty-materials'),
    path('create-material/<str:course_id>', renderCreateMaterialView, name='create-material'),
]