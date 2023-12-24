from django.db import models


class Risk(models.Model):
    STATUS_CHOICES = (
        ("not_mitigated", "NOT MITIGATED"),
        ("partially_mitigated", "PARTIALLY MITIGATED"),
        ("fully_mitigated", "FULLY MITIGATED"),
    )

    scenario = models.ForeignKey("risk.RiskScenario", on_delete=models.CASCADE)
    project = models.ForeignKey(
        "risk.Project", on_delete=models.CASCADE, related_name="risk"
    )
    status = models.CharField(max_length=32, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.project.name} - {self.scenario.name} - {self.status}"
