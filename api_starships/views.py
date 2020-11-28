from rest_framework import viewsets, permissions

from api_starships.models import Starship
from api_starships.serializers import StarshipSerializer


class StarShipsViewSet(viewsets.ModelViewSet):
    queryset = Starship.objects.all().order_by("hyperdrive_rating")
    serializer_class = StarshipSerializer
    permission_classes = [permissions.AllowAny,]

