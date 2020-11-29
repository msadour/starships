"""Account factories module."""
from typing import Any

import factory
from factory.faker import faker

from api_starships.models import Account, Starship


def generate_username(*args: Any) -> Any:
    """Return a random username.

    Args:
        args: Variable length argument list.

    Returns:
        A fake username.
    """
    fake = faker.Faker()
    return fake.profile(fields=["username"])["username"]


class AccountFactory(factory.django.DjangoModelFactory):
    """Class AccountFactory."""

    username = factory.LazyAttribute(generate_username)
    first_name = "test first name"
    last_name = "test last name"
    email = factory.LazyAttribute(generate_username)
    password = "qwertz"

    class Meta:
        """class Meta."""

        model = Account


class StarShipFactory(factory.django.DjangoModelFactory):
    """Class StarShipFactory."""

    hyperdrive_rating = 1.0
    name = "super starship"

    class Meta:
        """class Meta."""

        model = Starship
