from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView


class LoginRequiredTemplateView(LoginRequiredMixin, TemplateView):
    """
    View for login required templates
    """

    pass
