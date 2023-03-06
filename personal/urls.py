from django.urls import path

from .views import (
    renderHomeView,
    renderLogoutView,
    renderAvailableCoursesView,
)


urlpatterns = [
    path('', renderHomeView, name='home'),
    path('logout/', renderLogoutView, name='logout'),
    path('courses/', renderAvailableCoursesView, name='available-courses'),
]