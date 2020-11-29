"""Account factories module."""

import factory

from api_starships.models import Account, Starship


class AccountFactory(factory.django.DjangoModelFactory):
    """Class AccountFactory."""

    username = "username"
    first_name = "test first name"
    last_name = "test last name"
    email = "email@gmail.com"
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
