from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from risk.models import Project


class RiskTableHtmxView(LoginRequiredMixin, ListView):
    """
    View for displaying a table of Project summaries

    Permission "risk.view_project"
        - View all projects
    w/o Permission "risk.view_project"
        - View only projects owned by user
    """

    template_name = "risk/htmx/risk_table_htmx.html"
    queryset = Project.objects.get_summary()

    def get_queryset(self, **kwargs):
        if not self.request.user.has_perm("risk.view_project"):
            self.queryset = self.queryset.filter(owner=self.request.user)

        return super().get_queryset(**kwargs)
