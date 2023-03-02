from django.db import models
from django.contrib.auth.models import User

from personal.models import (
    FacultyRecord,
)

# Create your models here.


class Faculty(models.Model) :
    
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    record = models.OneToOneField(FacultyRecord, null=True, on_delete=models.SET_NULL)

    def __str__(self) :
        return self.record.name