from django.db import models
from django.db.models import Count, Q
from django.db.models.query import QuerySet


class ProjectManager(models.Manager):
    def get_summary(self) -> QuerySet:
        """
        Get summary of projects
            - sum of Unresolved High Severity
            - sum of Unresolved Risk
            - sum of Resolved Risk
            - sum of All Risk
        :return: Project QuerySet
        """
        unresolved_high_severity = Count(
            "risk",
            filter=~Q(risk__status="fully_mitigated")
            & Q(risk__scenario__severity="high"),
        )
        unresolved_risk = Count("risk", filter=~Q(risk__status="fully_mitigated"))
        resolved_risk = Count("risk", filter=Q(risk__status="fully_mitigated"))
        all_risk = Count("risk")
        return (
            self.annotate(unresolved_high_severity=unresolved_high_severity)
            .annotate(unresolved_risk=unresolved_risk)
            .annotate(resolved_risk=resolved_risk)
            .annotate(all_risk=all_risk)
        )
