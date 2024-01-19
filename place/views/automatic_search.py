from typing import Optional
from rest_framework import serializers, viewsets

from place.models.place import Place

from django_filters import rest_framework as filters
from django_filters.conf import settings
from django_filters.constants import EMPTY_VALUES
from place.models.reservation import ReserveSlot


class ReservationBasedFilter(filters.DateFromToRangeFilter):
    def filter(self, places, value):
        places = super().filter(places, value)
        if not self.filtered(places, value):
            return places
        return self.__get_available_places(places, value)
    
    def filtered(self, places, value):
        return self.process_value(value) not in EMPTY_VALUES

    def __get_available_places(self, places, value):
        reserved_places = self.__get_reserved_places(places, value)
        return places.exclude(code__in=reserved_places).distinct()
    
    def __get_reserved_places(self, places, value):
        value = self.process_value(value)
        lookup = "%s__%s" % (self.field_name, self.lookup_expr)
        return places.filter(**{
            lookup: value,
            "reserve_slots__status":ReserveSlot.ReserveSlotStatus.reserved
        })
    
    def process_value(self, value):
        if value:
            if value.start is not None and value.stop is not None:
                return (value.start, value.stop)
            elif value.start is not None:
                return value.start
            elif value.stop is not None:
                return value.stop
        return value


class BasicPlaceFilterSet(filters.FilterSet):
    reserve_date = ReservationBasedFilter(field_name="reserve_slots__date")

    def filter_queryset(self, queryset):
        queryset = super().filter_queryset(queryset)
        return queryset

    class Meta:
        model = Place
        fields = {
            "capacity": ["exact"],
            "rate": ["gte"],
            "area_size": ["lte", "gte"],
            # 'reserve_slots__date': ['lte', 'gte']
        }


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = "__all__"


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
