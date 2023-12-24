from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from risk.models import Risk


class RiskHtmxView(LoginRequiredMixin, UpdateView):
    fields = ["status"]
    model = Risk
    success_url = reverse_lazy("risk:risk_table")
