from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from risk.models import Risk


class RiskHtmxView(LoginRequiredMixin, UpdateView):
    """
    View to update Risk

    Permission "risk.change_risk"
        - POST to update Risk
    """

    fields = ["status"]
    model = Risk
    success_url = reverse_lazy("risk:risk_table")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_perm("risk.change_risk"):
            return super().dispatch(request, *args, **kwargs)
        else:
            return self.handle_no_permission()
