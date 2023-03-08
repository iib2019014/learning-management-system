from django.db import models


# from faculty.models import (
    # Faculty,
# )

# Create your models here.

MIN_CREDITS = 12


SEMESTER = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
    (6, 6),
    (7, 7),
    (8, 8),
)

DESIGNATION = (
    ('Prof', 'Professor'),
    ('Asst.Prof', 'Assistant Professor'),
    ('Asoc.Prof', 'Associate Professor'),
    ('TA', 'Teaching Assistant'),
)

DEPARTMENT = (
    ('IT', 'Information Technology'),
    ('IT-BI', 'Information Technology Business Informatics'),
    ('ECE', 'Electronics and Communication Engineering'),
)


class StudentRecord(models.Model) :
    name = models.CharField(max_length=255, blank=False)
    
    email = models.EmailField(max_length=255, blank=False)

    rollno = models.CharField(max_length=255, blank=False)

    semester = models.IntegerField(choices=SEMESTER)
    
    department = models.CharField(max_length=255, blank=False, choices=DEPARTMENT, default='IT-BI')

    def __str__(self) :
        return self.name

        
    def get_student(self) :

        if hasattr(self, 'student') :
            return self.student
        return None


class FacultyRecord(models.Model) :
    name = models.CharField(max_length=255, blank=False)
    
    email = models.EmailField(max_length=255, blank=False)

    designation = models.CharField(max_length=255, blank=False, choices=DESIGNATION)

    department = models.CharField(max_length=255, blank=False, choices=DEPARTMENT)

    def __str__(self) :
        return self.name
    

    def get_faculty(self) :

        if hasattr(self, 'faculty') :
            print("has")
            return self.faculty
        print("not has")
        return None


class Course(models.Model) :
    code = models.CharField(max_length=255, blank=False)

    title = models.CharField(max_length=255, blank=False)

    department = models.CharField(max_length=255, blank=False, choices=DEPARTMENT)

    credits = models.IntegerField(default=4)

    faculty = models.ForeignKey('faculty.Faculty', null=True, on_delete=models.SET_NULL)

    def __str__(self) :
        return self.title