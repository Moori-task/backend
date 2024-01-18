from rest_framework import serializers, viewsets

from place.models.place import Place


from django_filters import rest_framework as filters

class PlaceFilter(filters.FilterSet):
    class Meta:
        model = Place
        fields = {
            'capacity': ['exact'],
            'rate': ['gte'],
            'area_size': ['lte', 'gte']
        }

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'code']

class PlaceViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = []
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = PlaceFilter
    
    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)[:5]