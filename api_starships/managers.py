"""Managers module."""

from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom user model manager."""

    def create_user(self, **fields: Any) -> User:
        """Create and save a User.

        Args:
            fields: Arbitrary keyword arguments.

        Returns:
            User.
        """
        email = fields.get("email", "")
        username = fields.get("username", None)
        password = fields.get("password")

        email = email[0] if type(email) == list else email
        username = username[0] if type(username) == list else username
        password = password[0] if type(password) == list else password

        if not username:
            raise ValueError(_("The username must be set"))

        if "password_again" in fields.keys():
            if password != fields["password_again"]:
                raise ValueError(_("The two password are different."))
        fields.pop("password_again", None)
        fields["email"] = self.normalize_email(email)

        fields["email"] = (
            fields["email"][0] if type(fields["email"]) == list else fields["email"]
        )
        fields["username"] = (
            fields["username"][0]
            if type(fields["username"]) == list
            else fields["username"]
        )
        fields["password"] = (
            fields["password"][0]
            if type(fields["password"]) == list
            else fields["password"]
        )

        user = self.model(**fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        username: str = None,
        email: str = None,
        password: str = None,
        **extra_fields: Any
    ) -> User:
        """Create and save a SuperUser.

        Args:
            username:
            email:
            password:
            extra_fields: Arbitrary keyword arguments.

        Returns:
            User.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        extra_fields["username"] = username
        extra_fields["email"] = email if email else username
        extra_fields["password"] = password

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(**extra_fields)
