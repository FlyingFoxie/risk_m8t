from django.contrib.auth.models import User
from django.db import models


class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"
