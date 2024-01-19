from django.urls import path, include

from place.views.import_models import *
from .views import ImportPlaceView
from .views import PlaceViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"get", PlaceViewSet)

import_urlpatterns = [
    path("place/", ImportPlaceView.as_view()),
    path("reservation/", ImportReservationView.as_view()),
]
urlpatterns = [
    path("", include(router.urls)),
    # Other URL patterns
    path("import/", include(import_urlpatterns)),
]
