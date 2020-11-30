"""Urls module."""

from django.urls import path
from rest_framework.routers import DefaultRouter

from api_starships.views import (
    StarShipsViewSet,
    AccountViewSet,
    CustomAuthToken,
    LogoutViewSet,
)

router = DefaultRouter()
router.register(r"logout", LogoutViewSet, basename="logout")
router.register(r"starship", StarShipsViewSet, basename="all")
router.register(r"account", AccountViewSet, basename="account")

urlpatterns = router.urls

urlpatterns += [
    path("api-token-auth/", CustomAuthToken.as_view()),
]
