from django.db import models
from django.contrib.auth.models import AbstractUser


class StudentUser(AbstractUser):
    student_class = models.CharField(max_length=10)
    division = models.CharField(max_length=1)