from rest_framework.routers import DefaultRouter

from api_starships.views import StarShipsViewSet

router = DefaultRouter()
router.register(r"all", StarShipsViewSet, basename="all")

urlpatterns = router.urls
