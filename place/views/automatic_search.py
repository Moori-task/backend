from rest_framework import serializers, permissions, viewsets

from place.models.place import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ['id', 'code']

class PlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = []