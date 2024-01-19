from typing import Optional
from rest_framework import serializers, viewsets

from place.models.place import Place


from django_filters import rest_framework as filters
from django_filters.conf import settings
from place.models.reservation import ReserveSlot


class ReservationBasedFilter(filters.DateFromToRangeFilter):
    def filter(self, qs, value):
        qs = super().filter(qs, value)
        if self.__queried(qs, value):
            qs = self.__get_available_places(qs, value)
        return qs

    def __get_available_places(self, places, value):
        # assert queryset = Join Place, Reserve
        reserved_places = places.filter(
            reserve_slots__status=ReserveSlot.ReserveSlotStatus.reserved,
            reserve_slots__date__range=[value.start, value.stop],
        )
        available_places = places.exclude(code__in=reserved_places).distinct()
        return available_places

    def __queried(self, qs, value) -> bool:
        # It should figure out whether a request is queried by reservation_date
        # I checked out in the library and if there would be a querying,
        # lookup_expr will be set to sth other than "DEFAULT" after finished function
        # TODO improve
        return self.lookup_expr != settings.DEFAULT_LOOKUP_EXPR


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
