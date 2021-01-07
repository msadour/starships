"""Test starship module."""

from __future__ import absolute_import
import django

django.setup()

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
        """Test list of starships.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_starship)

        assert len(response.data) > 0

    def test_retrieve(self) -> None:
        """Test retrieve a starship.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_starship + f"{self.starship.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_add_favorite(self):
        """Test add a starship in favorite.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(url_starship + f"{self.starship.id}/add_favorite/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remove_favorite(self):
        """Test remove a starship in favorite.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(
            url_starship + f"{self.starship.id}/remove_favorite/"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_forbidden(self) -> None:
        """Test create a starship (forbidden).

        Raises:
            AssertError: Assertion failed.
        """
        data = """{
                "name": "test",
                "hyperdrive_rating": 1.0
            }"""

        response = self.client.post(
            url_starship, data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_forbidden(self) -> None:
        """Test delete a starship (forbidden).

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.delete(url_starship + str(self.starship.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_forbidden(self) -> None:
        """Test update a starship (forbidden).

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(
            url_starship + str(self.starship.id) + "/", data={"name": "new name"},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
