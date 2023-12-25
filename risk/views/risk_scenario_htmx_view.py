from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView

from risk.forms import RiskForm
from risk.models import Risk, RiskScenario


class RiskScenarioHtmxView(LoginRequiredMixin, ListView, FormView):
    template_name = "risk/htmx/risk_scenario_htmx.html"
    model = RiskScenario
    form_class = RiskForm
    success_url = reverse_lazy("risk:risk_scenario")

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs

    def form_valid(self, form):
        risk_scenario_object = get_object_or_404(
            RiskScenario, pk=self.request.POST.get("scenario")
        )
        if Risk.objects.filter(
            scenario=risk_scenario_object, project=form.cleaned_data["project"]
        ).exists():
            messages.error(
                self.request,
                f"{risk_scenario_object.name} already exists for {form.cleaned_data['project']}",
                extra_tags="danger",
            )
            return HttpResponseRedirect(self.get_success_url())

        new_risk = form.save(commit=False)
        new_risk.scenario = risk_scenario_object
        new_risk.status = "not_mitigated"
        new_risk.save()
        messages.info(
            self.request,
            f"{risk_scenario_object.name} created successfully for {form.cleaned_data['project']}",
        )

        return HttpResponseRedirect(self.get_success_url())
