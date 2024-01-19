from django.urls import path, include

from place.views.import_models import *
from .views import ImportPlace
from .views import PlaceViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"get", PlaceViewSet)

import_urlpatterns = [
    path("place/", ImportPlace.as_view()),
    path("reservation/", ImportReservation.as_view()),
]
urlpatterns = [
    path("", include(router.urls)),
    # Other URL patterns
    path("import/", include(import_urlpatterns)),
]
