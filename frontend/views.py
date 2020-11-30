import requests

from django.shortcuts import render


def list_starship(request):
    list_starship = requests.get("http://127.0.0.1:8000/api_starships/starship/").json()
    return render(request, "frontend/starships_list.html", {"list_starship": list_starship})
