"""Managers module."""

from typing import Any

from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """Custom user model manager where email is the unique identifiers for authentication instead of usernames."""

    def create_user(self, **fields: Any) -> User:
        """Create and save a User with the given email and password.

        Args:
            fields: Arbitrary keyword arguments.

        Returns:
            User.
        """
        email = fields.get("email", "")
        username = fields.get("username", None)
        password = fields.get("password")

        if not username:
            raise ValueError(_("The username must be set"))

        if "password_again" in fields.keys():
            if password != fields["password_again"]:
                raise ValueError(_("The two password are different."))
        fields.pop("password_again", None)
        fields["email"] = self.normalize_email(email)

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
        """Create and save a SuperUser with the given email and password.

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
