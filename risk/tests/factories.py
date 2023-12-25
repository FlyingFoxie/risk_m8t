import random
from collections.abc import Sequence
from typing import Any

from django.contrib.auth import get_user_model
from factory import Faker, post_generation
from factory.django import DjangoModelFactory

"""
The available types for Faker include:

    name: Generates a full name.
    first_name: Generates a first name.
    last_name: Generates a last name.
    email: Generates an email address.
    phone_number: Generates a phone number.
    address: Generates a street address.
    city: Generates a city name.
    state: Generates a state name.
    country: Generates a country name.
    zipcode: Generates a zip code.
    user_name: Generates a username.
    password: Generates a password.
    text: Generates random text.
    sentence: Generates a sentence.
    paragraph: Generates a paragraph.
"""


class UserFactory(DjangoModelFactory):
    username = Faker("user_name")
    email = "wcher@avodaq.com"

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs):
        password = (
            extracted
            if extracted
            else Faker(
                "password",
                length=42,
                special_chars=True,
                digits=True,
                upper_case=True,
                lower_case=True,
            ).evaluate(None, None, extra={"locale": None})
        )
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ["username"]
        skip_postgeneration_save = True


class ProjectFactory(DjangoModelFactory):
    name = Faker("name")

    class Meta:
        model = "risk.project"


class RiskFactory(DjangoModelFactory):
    status = random.choice(["not_mitigated", "partially_mitigated", "fully_mitigated"])

    class Meta:
        model = "risk.risk"


class RiskScenarioFactory(DjangoModelFactory):
    name = Faker("name")
    description = Faker("text")
    mitigation_strategy = Faker("text")
    severity = random.choice(["high", "medium", "low"])
    likelihood_of_attack = random.choice(["high", "medium", "low"])
    target = random.choice(["dataflow", "server", "process", "datastore"])

    class Meta:
        model = "risk.riskscenario"
