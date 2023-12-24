from django import forms

from risk.models import Project, Risk


class RiskForm(forms.ModelForm):
    class Meta:
        model = Risk
        fields = ["project"]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)

        self.fields["project"].queryset = Project.objects.filter(owner=user)
