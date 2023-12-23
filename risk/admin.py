from django.contrib import admin

from risk.models import Project, Risk, RiskScenario

admin.site.register(Risk)
admin.site.register(RiskScenario)
admin.site.register(Project)
