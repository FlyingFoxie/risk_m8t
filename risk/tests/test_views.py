from django.urls import reverse


class TestDashboardHtmxView:
    def test_dashboard_htmx_view_return_pm_html(
        self, project_manager_group, user, client
    ):
        user.groups.add(project_manager_group)
        user.save()

        client.force_login(user)
        response = client.get(reverse("risk:dashboard_htmx"))

        assert response.status_code == 200
        assert (
            "risk/htmx/dashboard/project_manager_dashboard.html"
            in response.template_name
        )

    def test_dashboard_htmx_view_return_rc_html(
        self, risk_consultant_group, user, client
    ):
        user.groups.add(risk_consultant_group)
        user.save()

        client.force_login(user)
        response = client.get(reverse("risk:dashboard_htmx"))

        assert response.status_code == 200
        assert (
            "risk/htmx/dashboard/risk_consultant_dashboard.html"
            in response.template_name
        )
