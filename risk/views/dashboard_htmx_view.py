from collections import Counter

import plotly.graph_objects as go
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from risk.models import Project


class DashboardHtmxView(LoginRequiredMixin, TemplateView):
    """
    View for displaying Dashboard

    Permission "risk.change_risk" and "risk.view_risk"
        - View Project Manager dashboard
    Permission "risk.view_risk
        - View Risk Consultant dashboard
    """

    template_name = "risk/htmx/dashboard/no_permission_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Project Manager Role
        if self.request.user.has_perm(
            "risk.change_risk"
        ) and self.request.user.has_perm("risk.view_risk"):
            self.template_name = "risk/htmx/dashboard/project_manager_dashboard.html"
            project_objects = (
                Project.objects.get_summary()
                .filter(owner=self.request.user)
                .prefetch_related("risk")
                .prefetch_related("risk__scenario")
            )
        # Risk Consultant Role
        elif self.request.user.has_perm("risk.view_risk"):
            self.template_name = "risk/htmx/dashboard/risk_consultant_dashboard.html"
            project_objects = (
                Project.objects.get_summary()
                .prefetch_related("risk")
                .prefetch_related("risk__scenario")
                .order_by("all_risk")
            )
            risk_scenario = [
                risk.scenario.name
                for project in project_objects
                for risk in project.risk.all()
            ]
            risk_scenario_counts = Counter(risk_scenario)

            risk_scenario_heatmap = [
                (
                    risk.scenario.name,
                    risk.scenario.created_datetime.strftime("%Y-%m-%d"),
                )
                for project in project_objects
                for risk in project.risk.all()
            ]
            risk_scenario_heatmap_counts = Counter(risk_scenario_heatmap)
            risk_scenario_heatmap_labels = list(risk_scenario_heatmap_counts.keys())
            risk_scenario_heatmap_values = list(risk_scenario_heatmap_counts.values())

            # Create a Heatmap
            fig_heatmap = go.Figure(
                data=go.Heatmap(
                    z=risk_scenario_heatmap_values,
                    x=[i[1] for i in risk_scenario_heatmap_labels],
                    y=[i[0] for i in risk_scenario_heatmap_labels],
                    colorscale="Viridis",
                )
            )

            # Create a Horizontal Bar chart
            fig_hor = go.Figure(
                data=[
                    go.Bar(
                        y=[project.name for project in project_objects],
                        x=[project.all_risk for project in project_objects],
                        orientation="h",
                    )
                ]
            )

            # Create a Pie chart
            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=list(risk_scenario_counts.keys()),
                        values=list(risk_scenario_counts.values()),
                        hole=0.3,
                    )
                ]
            )

            context["risk_scenario_pie_chart"] = fig.to_html()
            context["top_project_risk_bar_chart"] = fig_hor.to_html()
            context["risk_heat_map"] = fig_heatmap.to_html()
            context["risk_scenario_counts"] = dict(risk_scenario_counts)

        else:
            return context

        context["total_unresolved_high_severity_risk"] = sum(
            project.unresolved_high_severity for project in project_objects
        )
        context["total_unresolved_risk"] = sum(
            project.unresolved_risk for project in project_objects
        )

        return context
