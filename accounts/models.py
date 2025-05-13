from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    USER_ROLES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = models.CharField(max_length=10, choices=USER_ROLES)

    def is_student(self):
        return self.role == 'student'

    def is_instructor(self):
        return self.role == 'instructor'
