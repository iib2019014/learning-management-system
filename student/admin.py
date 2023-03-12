from django.contrib import admin

from .models import (
    Student,
    Submission,
)

# Register your models here.


admin.site.register(Student)
admin.site.register(Submission)