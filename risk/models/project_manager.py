from django.db import models
from django.db.models import Count, Q


class ProjectManager(models.Manager):
    def get_summary(self):
        unresolved_high_severity = Count(
            "risk",
            filter=~Q(risk__status="fully_mitigated")
            & Q(risk__scenario__severity="high"),
        )
        unresolved_risk = Count("risk", filter=~Q(risk__status="fully_mitigated"))
        return self.annotate(
            unresolved_high_severity=unresolved_high_severity
        ).annotate(unresolved_risk=unresolved_risk)
