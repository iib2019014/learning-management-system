import os

from django.db import models


from personal.models import (
    Course,
)


MATERIAL_TYPE = (
    ('file', 'file'),
    ('link', 'link'),
)

# Create your models here.


def custom_upload_to_materials(instance, filename) :
    print("yay")
    return os.path.join(instance.course.code + '/materials/', filename)


def custom_upload_to_assignments(instance, filename) :
    return os.path.join(instance.course.code + '/assignments/', filename)


class Material(models.Model) :

    name = models.CharField(max_length=255, blank=False)

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE, blank=False)

    link = models.CharField(max_length=255, blank=True)

    file = models.FileField(blank=True, upload_to=custom_upload_to_materials)

    def __str__(self) :
        return f'material {self.id}, {self.course}'


class Assignment(models.Model) :

    name = models.CharField(max_length=255, blank=False)

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    file = models.FileField(upload_to=custom_upload_to_assignments)

    def __str__(self) :
        return f'assignment {self.id}, {self.course}'