from django.urls import path

from .views import (
    renderHomeView,
    renderLogoutView,
)


urlpatterns = [
    path('', renderHomeView, name='home'),
    path('logout/', renderLogoutView, name='logout'),
]