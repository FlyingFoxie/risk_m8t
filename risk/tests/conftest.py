import random

import pytest
from django.contrib.auth.models import Group

from risk.tests.factories import (
    ProjectFactory,
    RiskFactory,
    RiskScenarioFactory,
    UserFactory,
)


@pytest.fixture
def user(db):
    return UserFactory()


@pytest.fixture
def project(db, user):
    return ProjectFactory(owner=user)


@pytest.fixture
def risk_scenario(db, user):
    return RiskScenarioFactory(created_by=user)


@pytest.fixture
def risk_scenarios(db, user):
    return [
        RiskScenarioFactory(
            created_by=user, id=i, severity=random.choice(["high", "medium", "low"])
        )
        for i in range(1, 10)
    ]


@pytest.fixture
def risk(db, project, risk_scenario):
    return RiskFactory(project=project, scenario=risk_scenario)


@pytest.fixture
def risks(db, project, risk_scenarios):
    return [
        RiskFactory(
            project=project,
            scenario=risk_scenario,
            status=random.choice(
                ["not_mitigated", "partially_mitigated", "fully_mitigated"]
            ),
        )
        for risk_scenario in risk_scenarios
    ]


@pytest.fixture
def project_manager_group(db):
    return Group.objects.create(name="Project Manager")


@pytest.fixture
def risk_consultant_group(db):
    return Group.objects.create(name="Risk Consultant")
