from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, UpdateView

from risk.models import Project, Risk


class ProjectHtmxView(LoginRequiredMixin, DetailView, UpdateView):
    """
    View to generate Project Detail modal from Risk Table
    """

    template_name = "risk/htmx/project_htmx.html"
    queryset = (
        Project.objects.prefetch_related("risk")
        .prefetch_related("risk__scenario")
        .all()
    )
    fields = ["status"]
    model = Risk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["mitigated_risks"] = self.get_object().risk.filter(
            status="fully_mitigated"
        )
        context["not_mitigated_risks"] = self.get_object().risk.exclude(
            status="fully_mitigated"
        )

        return context
