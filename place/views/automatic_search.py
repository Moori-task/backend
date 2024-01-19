from typing import Optional
from rest_framework import serializers, viewsets

from place.models.place import Place


from django_filters import rest_framework as filters

from place.models.reservation import ReserveSlot

class BasicPlaceFilterSet(filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'capacity': ['exact'],
            'rate': ['gte'],
            'area_size': ['lte', 'gte']
        }

class ReserveBasedPlaceFilterSet(filters.FilterSet):
    def __init__(self, base_filter_set: "filters.FilterSet", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__base_filter_set = base_filter_set
    
    def filter_queryset(self, queryset):
        queryset = self.__base_filter_set.filter_queryset(queryset)
        queryset = super().filter_queryset(queryset)
        if self.__queried(queryset):
            queryset = self.__get_available_places(queryset)
        return queryset
    
    def __get_available_places(self, queryset):
        # assert queryset = Join Place, Reserve
        reserved_places = queryset.filter(status=ReserveSlot.ReserveSlotStatus.reserved).distinct()
        places = queryset.distinct()
        available_places = places.exclude(code__in=reserved_places)
        return available_places
    
    def __queried(self, queryset) -> bool:
        # It should figure out whether a request is queried by reservation
        # return queryset = Join Place, Reserve
        # TODO improve
        return True
    
    class Meta:
        model = Place
        fields = {
            'reserved_slot__date': ['lte', 'gte']
        }
    

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = []
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BasicPlaceFilterSet
    
    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)[:5]