"""Urls modules."""

from django.urls import path

from frontend.views.authentication import (
    authentication_page,
    login,
    logout,
    subscription,
    subscription_page,
)
from frontend.views.starship import (
    list_starship,
    favorite_starship,
    add_favorite,
    remove_favorite,
)

urlpatterns = [
    path("", list_starship),
    path("favorite", favorite_starship, name="favorite"),
    path("add_favorite/<int:id_starship>", add_favorite, name="add_favorite"),
    path("remove_favorite/<int:id_starship>", remove_favorite, name="remove_favorite"),
    path("authentication", authentication_page, name="authentication"),
    path("subscription", subscription, name="subscription"),
    path("subscription_page", subscription_page, name="subscription_page"),
    path("login", login),
    path("logout", logout, name="logout"),
]
