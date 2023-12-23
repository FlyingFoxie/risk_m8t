from django.contrib.auth.models import User
from django.db import models


class RiskScenario(models.Model):
    LEVEL_CHOICES = (("high", "HIGH"), ("medium", "MEDIUM"), ("low", "LOW"))

    TARGET_CHOICES = (
        ("dataflow", "DATAFLOW"),
        ("server", "SERVER"),
        ("process", "PROCESS"),
        ("datastore", "DATASTORE"),
    )

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    name = models.CharField(max_length=128)
    description = models.TextField()
    mitigation_strategy = models.TextField()
    severity = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    likelihood_of_attack = models.CharField(max_length=32, choices=LEVEL_CHOICES)
    target = models.CharField(max_length=32, choices=TARGET_CHOICES)

    created_datetime = models.DateTimeField(auto_now_add=True)
    updated_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
