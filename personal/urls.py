from django.urls import path

from .views import (
    renderHomeView,
)


urlpatterns = [
    path('', renderHomeView, name='home'),
]