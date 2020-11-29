"""Models."""

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from api_starships.managers import CustomUserManager


class Starship(models.Model):
    """Class Starship."""

    hyperdrive_rating = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    name = models.CharField(max_length=255, null=False)

    def get_total_favorite_user(self) -> int:
        """Return the number of people that add this starship as favorite.

        Returns:
            Number of added in favorite.
        """
        return len(self.user_favorite.all())


class Account(AbstractBaseUser):
    """Class Account."""

    username = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    starships_favorite = models.ManyToManyField(Starship, blank=True, related_name="user_favorite")

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
