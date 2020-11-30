from django.urls import path

from frontend.views import list_starship

urlpatterns = [
    path("", list_starship)
]
