from django.db import models


from personal.models import (
    Course,
)


MATERIAL_TYPE = (
    ('file', 'file'),
    ('link', 'link'),
)

# Create your models here.


class Material(models.Model) :

    name = models.CharField(max_length=255, blank=False)

    course = models.ForeignKey(Course, null=True, on_delete=models.SET_NULL)

    material_type = models.CharField(max_length=10, choices=MATERIAL_TYPE)

    link = models.CharField(max_length=255, blank=True)

    file = models.FileField(blank=True)

    # def __str__(self) :
    #     return 