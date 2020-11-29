"""Serializer."""

from django.contrib.auth.hashers import check_password
from rest_framework import serializers

from .models import Starship, Account


class StarshipSerializer(serializers.ModelSerializer):
    """Class StarshipSerializer."""

    class Meta:
        """Class Meta."""

        model = Starship
        fields = [
            "id",
            "name",
            "hyperdrive_rating",
            "get_total_favorite_user"
        ]


class AccountSerializer(serializers.ModelSerializer):
    """Class AccountSerializer."""

    class Meta:
        """Class Meta."""

        model = Account
        fields = '__all__'


class AuthTokenSerializer(serializers.Serializer):
    """class AuthTokenSerializer."""

    username = serializers.CharField()
    password = serializers.CharField(
        style={"input_type": "password"}, trim_whitespace=False
    )

    def authenticate_user(self, username: str = None, password: str = None):
        """Authenticate a user.

        Args:
            username:
            password:

        Returns:
            User.
        """
        try:
            user = Account.objects.get(username=username)
            if check_password(password, user.password):
                return user
            else:
                return None
        except Exception:
            return None

    def validate(self, attrs):
        """Validate a user.

        Args:
            attrs: Arbitrary keyword arguments.
        Returns:
            User.
        """
        username = attrs.get("username")
        password = attrs.get("password")
        user = self.authenticate_user(username=username, password=password)
        if not user:
            msg = "Unable to authenticate with provided credentials"
            raise serializers.ValidationError(msg, code="authorization")

        return user
