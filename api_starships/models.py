from django.db import models


class Starship(models.Model):
    """Class Starship."""

    hyperdrive_rating = models.DecimalField(max_digits=2, decimal_places=1, default=1.0)
    name = models.CharField(max_length=255, null=False)
