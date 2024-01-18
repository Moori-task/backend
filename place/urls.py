from django.urls import path
from .views import import_from_excel

urlpatterns = [
    # Other URL patterns
    path('import/', import_from_excel, name='import_from_excel'),
]