from django.urls import resolve, reverse


class TestURLName:
    def test_risk_dashboard_url(self):
        assert reverse("risk:dashboard") == "/risk/dashboard"
        assert resolve("/risk/dashboard").view_name == "risk:dashboard"

    def test_risk_dashboard_htmx_url(self):
        assert reverse("risk:dashboard_htmx") == "/risk/dashboard_htmx"
        assert resolve("/risk/dashboard_htmx").view_name == "risk:dashboard_htmx"

    def test_risk_scenario_url(self):
        assert reverse("risk:risk_scenario") == "/risk/risk_scenario"
        assert resolve("/risk/risk_scenario").view_name == "risk:risk_scenario"

    def test_risk_scenario_htmx_url(self):
        assert reverse("risk:risk_scenario_htmx") == "/risk/risk_scenario_htmx"
        assert (
            resolve("/risk/risk_scenario_htmx").view_name == "risk:risk_scenario_htmx"
        )

    def test_risk_table_url(self):
        assert reverse("risk:risk_table") == "/risk/risk_table"
        assert resolve("/risk/risk_table").view_name == "risk:risk_table"

    def test_risk_table_htmx_url(self):
        assert reverse("risk:risk_table_htmx") == "/risk/risk_table_htmx"
        assert resolve("/risk/risk_table_htmx").view_name == "risk:risk_table_htmx"

    def test_risk_project_htmx_url(self, project):
        assert (
            reverse("risk:project_htmx", kwargs={"pk": project.pk})
            == f"/risk/project_htmx/{project.pk}"
        )
        assert (
            resolve(f"/risk/project_htmx/{project.pk}").view_name == "risk:project_htmx"
        )

    def test_risk_htmx_url(self, risk):
        assert (
            reverse("risk:risk_htmx", kwargs={"pk": risk.pk})
            == f"/risk/risk_htmx/{risk.pk}"
        )
        assert resolve(f"/risk/risk_htmx/{risk.pk}").view_name == "risk:risk_htmx"

    def test_risk_delete_url(self, risk):
        assert (
            reverse("risk:risk_delete", kwargs={"pk": risk.pk})
            == f"/risk/risk_delete/{risk.pk}"
        )
        assert resolve(f"/risk/risk_delete/{risk.pk}").view_name == "risk:risk_delete"
