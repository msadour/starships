"""Views module."""

from typing import Any

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import logout as django_logout
from rest_framework import viewsets, permissions, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import action, permission_classes
from django.conf import settings
from rest_framework.request import Request
from rest_framework.response import Response

from api_starships.models import Starship, Account
from api_starships.permissions import StarshipPermission, AccountPermission
from api_starships.serializers import (
    StarshipSerializer,
    AccountSerializer,
    AuthTokenSerializer,
)


class StarShipsViewSet(viewsets.ModelViewSet):
    """Class StarShipsViewSet."""

    queryset = Starship.objects.all().order_by("hyperdrive_rating")
    serializer_class = StarshipSerializer
    permission_classes = (StarshipPermission,)

    @action(detail=True, methods=["patch"], url_path="add_favorite")
    def add_favorite(self, request: Request, pk: int = None) -> Response:
        """Add a starship as favorite for a user.

        Args:
            request: request sent by the client.
            pk: Id of the starship.

        Returns:
            Response from the server.
        """
        starship = Starship.objects.get(id=pk)
        request.user.starships_favorite.add(starship)
        return Response(status=status.HTTP_200_OK)

    @action(detail=True, methods=["patch"], url_path="remove_favorite")
    def remove_favorite(self, request: Request, pk: int = None) -> Response:
        """Remove a starship in favorite for a user.

        Args:
            request: request sent by the client.
            pk: Id of the starship.

        Returns:
            Response from the server.
        """
        starship = Starship.objects.get(id=pk)
        request.user.starships_favorite.remove(starship)
        return Response(status=status.HTTP_200_OK)


class AccountViewSet(viewsets.ModelViewSet):
    """Class AccountViewSet."""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = (AccountPermission,)

    def create(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create a member.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
            kwargs: Arbitrary keyword arguments.

        Returns:
            Response from the server.
        """
        new_person = Account.objects.create_user(**request.data)
        serializer = AccountSerializer(new_person)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@permission_classes((permissions.AllowAny,))
class CustomAuthToken(ObtainAuthToken):
    """Class CustomAuthToken."""

    authentication_classes = [TokenAuthentication]

    def post(self, request: Request, *args: Any, **kwargs: Any) -> Response:
        """Create token for authentication.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
        Returns:
            Response from the server.
        """
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            request.user = user

            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {"token": token.key, "username": user.username, "account_id": user.id,}
            )
        return Response(status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class LogoutViewSet(viewsets.ViewSet):
    """Class LogoutViewSet."""

    def create(self, request: Request, *args: Any, **kwargs: Any):
        """Log out.

        Args:
            request: request sent by the client.
            args: Variable length argument list.
        Returns:
            Response from the server.
        """
        return self.logout(request)

    def logout(self, request: Request) -> Response:
        """Log out.

        Args:
            request: request sent by the client.
        Returns:
            Response from the server.
        """
        try:
            request.user.auth_token.delete()
        except (AttributeError, ObjectDoesNotExist):
            pass
        if getattr(settings, "REST_SESSION_LOGIN", True):
            django_logout(request)

        response = Response(
            {"detail": "Successfully logged out."},
            status=status.HTTP_200_OK,
            headers={"Access-Control-Allow-Credentials": True},
        )

        return response
