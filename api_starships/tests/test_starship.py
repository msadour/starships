"""Test starship module."""

from __future__ import absolute_import
import django;django.setup()


from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api_starships.tests.factories import AccountFactory, StarShipFactory

client = APIClient()

url_starship = "/api_starships/starship/"


class AccountTestCase(APITestCase):
    """class AccountTestCase."""

    def setUp(self) -> None:
        """Set up attributes for tests."""
        self.client = APIClient()
        self.account = AccountFactory()
        self.starship = StarShipFactory()
        self.client.force_authenticate(user=self.account)

    def test_list(self) -> None:
        """Test list of starship.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_starship)

        assert len(response.data) > 0

    def test_retrieve(self) -> None:
        """Test retrieve an starship.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_starship + f"{self.starship.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_favorite(self):
        """Test add an starship in favorite.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(url_starship + f"{self.starship.id}/add_favorite/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_favorite(self):
        """Test remove an starship in favorite.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(url_starship + f"{self.starship.id}/remove_favorite/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
