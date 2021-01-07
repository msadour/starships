"""View module."""

from typing import Any
import requests

from django.shortcuts import render
from api_starships.models import Account


def list_starship(request: Any) -> render:
    """Go to the list starships page.

    Args:
        request: request sent by the client.

    Returns:
        Render to the star ships page.
    """
    list_starship = requests.get("http://127.0.0.1:8000/api_starships/starship/").json()
    token = request.session.get("token", None)
    favorite_starships = []
    if request.session.get("id"):
        favorite_starships = [
            starship.id
            for starship in Account.objects.get(id=request.session["id"]).starships_favorite.all()
        ]
    return render(
        request,
        "frontend/starships_list.html",
        {"list_starship": list_starship, "token": token, "favorite_starships": favorite_starships},
    )


def favorite_starship(request: Any) -> render:
    """Go to the favorite star ships page.

    Args:
        request: request sent by the client.

    Returns:
        Render to the favorite star ships page.
    """
    id_user = request.session.get("id", None)
    response = requests.get(
        "http://127.0.0.1:8000/api_starships/account/" + str(id_user)
    ).json()
    starships_favorite = response["starships_favorite"]
    return render(
        request, "frontend/favorite.html", {"starships_favorite": starships_favorite}
    )


def add_favorite(request, id_starship: int = None) -> render:
    """Add a starship as favorite.

    Args:
        request: request sent by the client.
        id_starship:

    Returns:
        Render to the list star ships page.
    """
    requests.patch(
        "http://127.0.0.1:8000/api_starships/starship/"
        + str(id_starship)
        + "/add_favorite/",
        headers={"Authorization": "Token " + request.session["token"]},
    )
    return favorite_starship(request)


def remove_favorite(request, id_starship: int = None) -> render:
    """Add a starship as favorite.

    Args:
        request: request sent by the client.
        id_starship:

    Returns:
        Render to the list star ships page.
    """
    requests.patch(
        "http://127.0.0.1:8000/api_starships/starship/"
        + str(id_starship)
        + "/remove_favorite/",
        headers={"Authorization": "Token " + request.session["token"]},
    )
    return favorite_starship(request)
