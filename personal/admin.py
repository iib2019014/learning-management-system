from django.contrib import admin

from .models import (
    StudentRecord,
    FacultyRecord,
    Course,
)

# Register your models here.


class CourseAdmin(admin.ModelAdmin) :
    list_display = ('code', 'title', 'department')

    search_fields = ('code', 'title', 'department')

    ordering = ('code', 'title', 'department')

    filter_horizontal				= ()
    list_filter                     = ()
    fieldsets                       = ()


admin.site.register(StudentRecord)
admin.site.register(FacultyRecord)
admin.site.register(Course, CourseAdmin)