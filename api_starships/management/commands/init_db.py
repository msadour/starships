"""Command for init the databases."""

import os
import random
import time
from typing import Any

import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from api_starships.models import Starship, Account

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Command(BaseCommand):
    """Class command."""

    def handle(self, *args: Any, **options: Any) -> None:
        """Execute the command that cinit the database.

        Args:
            args: Variable length argument list.
            options: Arbitrary keyword arguments.
        """

        def delete_data() -> None:
            """Clean database."""
            Account.objects.all().delete()
            Starship.objects.all().delete()

        try:
            url = "https://en.wikipedia.org/wiki/List_of_Star_Wars_spacecraft"

            response_starships = requests.get(url)
            if response_starships.ok:
                soup = BeautifulSoup(response_starships.text, 'lxml')
                starships = soup.findAll('h3')
                for num, ship in enumerate(starships):
                    print(str(num + 1) + "/" + str(len(starships)))
                    try:
                        name = ship.find("span", class_="mw-headline").text

                        Starship.objects.create(
                            name=name,
                            hyperdrive_rating=round(random.uniform(0.5, 4.0), 1)
                        )
                    except Exception:
                        pass
                    time.sleep(10)
                time.sleep(10)

        except Exception as e:
            delete_data()
            self.stdout.write(e)
        else:
            self.stdout.write("The database has been (re)initialized.")
