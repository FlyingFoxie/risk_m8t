from risk.models import Project, Risk


class TestProjectModel:
    def test_project_manager_get_summary(self, risks):
        risk_objs = Risk.objects.all()
        unresolved_high_severity = (
            risk_objs.filter(scenario__severity="high")
            .exclude(status="fully_mitigated")
            .count()
        )
        unresolved_risk = risk_objs.exclude(status="fully_mitigated").count()
        resolved_risk = risk_objs.filter(status="fully_mitigated").count()
        all_risk = risk_objs.count()

        project_obj = Project.objects.get_summary()[0]
        assert project_obj.unresolved_high_severity == unresolved_high_severity
        assert project_obj.unresolved_risk == unresolved_risk
        assert project_obj.resolved_risk == resolved_risk
        assert project_obj.all_risk == all_risk
