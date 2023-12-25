from django.urls import path

from . import views

app_name = "risk"
urlpatterns = [
    path(
        "dashboard",
        views.LoginRequiredTemplateView.as_view(template_name="risk/dashboard.html"),
        name="dashboard",
    ),
    path("dashboard_htmx", views.DashboardHtmxView.as_view(), name="dashboard_htmx"),
    path(
        "risk_scenario",
        views.LoginRequiredTemplateView.as_view(
            template_name="risk/risk_scenario.html"
        ),
        name="risk_scenario",
    ),
    path(
        "risk_scenario_htmx",
        views.RiskScenarioHtmxView.as_view(),
        name="risk_scenario_htmx",
    ),
    path(
        "risk_table",
        views.LoginRequiredTemplateView.as_view(template_name="risk/risk_table.html"),
        name="risk_table",
    ),
    path("risk_table_htmx", views.RiskTableHtmxView.as_view(), name="risk_table_htmx"),
    path("project_htmx/<int:pk>", views.ProjectHtmxView.as_view(), name="project_htmx"),
    path("risk_htmx/<int:pk>", views.RiskHtmxView.as_view(), name="risk_htmx"),
    path("risk_delete/<int:pk>", views.RiskDeleteView.as_view(), name="risk_delete"),
]
