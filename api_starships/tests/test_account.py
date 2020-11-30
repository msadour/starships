"""Test account module."""

from __future__ import absolute_import
import django ; django.setup()

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from api_starships.tests.factories import AccountFactory

client = APIClient()

url_account = "/api_starships/account/"


class AccountTestCase(APITestCase):
    """class AccountTestCase."""

    def setUp(self) -> None:
        """Set up attributes for tests."""
        self.client = APIClient()
        self.account = AccountFactory()
        self.another_account = AccountFactory()
        self.client.force_authenticate(user=self.account)

    def test_list(self) -> None:
        """Test list of account.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_account)

        assert len(response.data) > 0

    def test_retrieve(self) -> None:
        """Test retrieve an account.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.get(url_account + f"{self.account.id}/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create(self) -> None:
        """Test create an account.

        Raises:
            AssertError: Assertion failed.
        """
        data_account = """{
          "username": "member@gmail.com",
          "email": "member@gmail.com",
          "password": "qwertz",
          "first_name": "fname2",
          "last_name": "lname2"
        }"""

        response = self.client.post(
            url_account, data=data_account, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete(self) -> None:
        """Test delete an account.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.delete(url_account + str(self.account.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_partial_update(self) -> None:
        """Test update an account.

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(
            url_account + str(self.account.id) + "/",
            data={"first_name": "new first name"},
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_forbidden(self) -> None:
        """Test delete an account from another user (forbidden).

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.delete(url_account + str(self.another_account.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_partial_update_forbidden(self) -> None:
        """Test update an account from another user (forbidden).

        Raises:
            AssertError: Assertion failed.
        """
        response = self.client.patch(
            url_account + str(self.another_account.id) + "/",
            data={"first_name": "new first name"},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
