from django.urls import path

from .views import (
    renderStudentHomeView,
    renderStudentRegistrationView,
    renderStudentLoginView,
    # renderCoursesView,
    renderAvailableCoursesView,
    renderCourseView,
    renderClassPeopleView,
    renderMaterialsView,
    renderAssignmentsView,
    renderAssignmentSubmissionView,
)

urlpatterns = [
    path('', renderStudentHomeView, name='student-home'),
    path('register/', renderStudentRegistrationView, name='student-register'),
    path('login/', renderStudentLoginView, name='student-login'),
    # path('courses/', renderCoursesView, name='student-courses'),
    path('enrollment/', renderAvailableCoursesView, name='available-courses'),
    path('course/<str:course_id>', renderCourseView, name='course'),
    path('class/<str:course_id>', renderClassPeopleView, name='people'),
    path('materials/<str:course_id>', renderMaterialsView, name='student-materials'),
    path('assignments/<str:course_id>', renderAssignmentsView, name='student-assignments'),
    path('assignment-submit/<str:assignment_id>', renderAssignmentSubmissionView, name='submit-assignment'),
]