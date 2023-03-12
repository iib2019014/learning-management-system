from django.db import models
from django.contrib.auth.models import User


from course.models import (
    Assignment
)

from personal.models import (
    StudentRecord,
    Course,
)

# Create your models here.



class Student(models.Model) :


    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    record = models.OneToOneField(StudentRecord, null=True, on_delete=models.SET_NULL)

    courses = models.ManyToManyField(Course, blank=True)

    enrolled = models.BooleanField(default=False)


    def __str__(self) :
        return self.record.name
    


class Submission(models.Model) :

    student = models.ForeignKey(Student, null=True, on_delete=models.SET_NULL)

    assignment = models.ForeignKey(Assignment, null=True, on_delete=models.SET_NULL)

    submitted = models.BooleanField(default=False)

    late = models.BooleanField(default=False)


    def __str__(self) :
        return f'{self.student}, {self.assignment}'