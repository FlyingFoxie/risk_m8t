from risk.forms import RiskForm


class TestRiskForm:
    def test_form_valid(self, project, risk_scenario):
        form = RiskForm(
            {"scenario": risk_scenario, "project": project, "status": "not_mitigated"},
            user=project.owner,
        )
        assert form.is_valid()
