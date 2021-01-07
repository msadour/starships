"""Views modules."""

from typing import Any

import requests

from django.shortcuts import render

from frontend.views.starship import list_starship


def authentication_page(request, error: Any = None) -> render:
    """Go to the authentication page.

    Args:
        request: request sent by the client.
        error: Errors when the credentials given are false.

    Returns:
        Render to the authentication page.
    """
    return render(request, "frontend/authentication.html", {"error": error})


def subscription_page(request, error: Any = None) -> render:
    """Go to the subscription page.

    Args:
        request: request sent by the client.
        error: Errors when the credentials given are false.

    Returns:
        Render to the subscription page.
    """
    return render(request, "frontend/subscription.html", {"error": error})


def subscription(request: Any) -> render:
    """Create an account.

    Args:
        request: request sent by the client.

    Returns:
        Render to the list of  starship page.
    """
    data_user = {
        "username": request.POST.get("username"),
        "email": request.POST.get("email"),
        "first_name": request.POST.get("first_name"),
        "last_name": request.POST.get("last_name"),
        "password": request.POST.get("password"),
    }
    response = requests.post(
        "http://127.0.0.1:8000/api_starships/account/", data=data_user
    )
    if response.status_code == 400:
        return subscription_page(request, error=True)
    data_login = {
        "username": request.POST.get("username"),
        "password": request.POST.get("password"),
    }
    response_login = requests.post(
        "http://127.0.0.1:8000/api_starships/api-token-auth/", data=data_login
    )
    response_login = response_login.json()
    request.session["token"] = response_login["token"]
    request.session["username"] = response_login["username"]
    request.session["id"] = response_login["account_id"]
    return list_starship(request)


def login(request: Any) -> render:
    """Authenticate an account.

    Args:
        request: request sent by the client.

    Returns:
        Render to the authentication page if error else list of starship list page.
    """
    data_login = {
        "username": request.POST.get("username"),
        "password": request.POST.get("password"),
    }
    response = requests.post(
        "http://127.0.0.1:8000/api_starships/api-token-auth/", data=data_login
    )
    if response.status_code == 400:
        return authentication_page(request, error=True)
    response = response.json()
    request.session["token"] = response["token"]
    request.session["username"] = response["username"]
    request.session["id"] = response["account_id"]
    return list_starship(request)


def logout(request: Any) -> render:
    """Logout an account.

    Args:
        request: request sent by the client.

    Returns:
        Render to the list of starship list page.
    """
    requests.post(
        "http://127.0.0.1:8000/api_starships/logout/",
        headers={"Authorization": "Token " + request.session["token"]},
    )
    request.session.clear()
    return list_starship(request)
