from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_EMPLOYEE = "EMPLOYEE"
    ROLE_MANAGER = "MANAGER"
    ROLE_CHOICES = ((ROLE_EMPLOYEE, "Employee"), (ROLE_MANAGER, "Manager"))
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_EMPLOYEE)
    manager = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL, related_name="team")
