from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView

from risk.models import RiskScenario


class RiskScenarioHtmxView(LoginRequiredMixin, ListView):
    template_name = "risk/htmx/risk_scenario_htmx.html"
    model = RiskScenario
