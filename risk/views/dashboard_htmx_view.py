from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class DashboardHtmxView(LoginRequiredMixin, TemplateView):
    def get_template_names(self):
        if self.request.user.groups.filter(name="Project Manager").exists():
            self.template_name = "risk/htmx/dashboard/project_manager_dashboard.html"
        elif self.request.user.groups.filter(name="Risk Consultant").exists():
            self.template_name = "risk/htmx/dashboard/risk_consultant_dashboard.html"
        return [self.template_name]
