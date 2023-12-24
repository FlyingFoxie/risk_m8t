from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LoginRequiredTemplateView(LoginRequiredMixin, TemplateView):
    pass
