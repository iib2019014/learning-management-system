from django.urls import path

from .views import (
    renderStudentHomeView,
    renderStudentRegistrationView,
    renderStudentLoginView,
    # renderCoursesView,
    renderAvailableCoursesView,
)

urlpatterns = [
    path('', renderStudentHomeView, name='student-home'),
    path('register/', renderStudentRegistrationView, name='student-register'),
    path('login/', renderStudentLoginView, name='student-login'),
    # path('courses/', renderCoursesView, name='student-courses'),
    path('enrollment/', renderAvailableCoursesView, name='available-courses'),
]