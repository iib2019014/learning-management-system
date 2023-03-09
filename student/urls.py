from django.urls import path

from .views import (
    renderStudentHomeView,
    renderStudentRegistrationView,
    renderStudentLoginView,
    # renderCoursesView,
    renderAvailableCoursesView,
    renderCourseView,
    renderMaterialsView,
)

urlpatterns = [
    path('', renderStudentHomeView, name='student-home'),
    path('register/', renderStudentRegistrationView, name='student-register'),
    path('login/', renderStudentLoginView, name='student-login'),
    # path('courses/', renderCoursesView, name='student-courses'),
    path('enrollment/', renderAvailableCoursesView, name='available-courses'),
    path('course/<str:course_id>', renderCourseView, name='course'),
    path('materials/<str:course_id>', renderMaterialsView, name='student-materials'),
]