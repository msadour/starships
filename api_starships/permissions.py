"""Permissions."""

from typing import Any

from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.viewsets import ModelViewSet


class StarshipPermission(permissions.BasePermission):
    """Class StarshipPermission."""

    def has_permission(self, request: Request, view: ModelViewSet) -> Any:
        """Check permission, for CRUD.

        Args:
            request: request sent by the client.
            view: Variable length argument list.

        Returns:
            Boolean that check if user has permission for CRUD.
        """
        if request.method == "GET":
            return True

        if request.method == "PATCH":
            if "add_favorite" in request.path or "remove_favorite" in request.path:
                return True
        return False

    # def has_object_permission(
    #     self, request: Request, view: ModelViewSet, obj: Any
    # ) -> Any:
    #     """Check permission, for CRUD, for one object.
    #
    #     Args:
    #         request: request sent by the client.
    #         view: Variable length argument list.
    #         obj:
    #
    #     Returns:
    #         Boolean that check if user has permission for CRUD.
    #     """
    #     if request.method == "PATCH":
    #         if "add_favorite" in request.path or "remove_favorite" in request.path:
    #             return True
    #     elif request.method == "GET":
    #         return True
    #
    #     return False


class AccountPermission(permissions.BasePermission):
    """Class StarshipPermission."""

    # def has_permission(
    #     self, request: Request, view: ModelViewSet
    # ) -> Any:
    #     """Check permission, for CRUD.
    #
    #     Args:
    #         request: request sent by the client.
    #         view: Variable length argument list.
    #
    #     Returns:
    #         Boolean that check if user has permission for CRUD.
    #     """
    #     return True

    def has_object_permission(
        self, request: Request, view: ModelViewSet, obj: Any
    ) -> Any:
        """Check permission, for CRUD, for one object.

        Args:
            request: request sent by the client.
            view: Variable length argument list.
            obj:

        Returns:
            Boolean that check if user has permission for CRUD.
        """
        if request.method in ["DELETE", "PATCH"]:
            return request.user.id == obj.id

        return True
