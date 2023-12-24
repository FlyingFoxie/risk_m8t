from django.contrib.auth.models import User
from django.db import models

from .project_manager import ProjectManager


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128)

    objects = ProjectManager()

    def __str__(self):
        return f"{self.name}"
