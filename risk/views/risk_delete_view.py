from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from risk.models import Risk


class RiskDeleteView(LoginRequiredMixin, DeleteView):
    """
    View to delete Risk

    Permission "risk.change_risk"
        - POST to delete Risk
    """

    model = Risk
    success_url = reverse_lazy("risk:risk_table")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_perm("risk.change_risk"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()
