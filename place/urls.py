from django.urls import path, include
from .views import import_from_excel
from .views import PlaceViewSet

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'get', PlaceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # Other URL patterns
    path('import/', import_from_excel, name='import_from_excel'),
    *router.urls
]