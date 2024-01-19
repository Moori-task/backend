import django
from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import views

# Create your views here.
from place.models import Place
import tablib


class ImportPlace(views.APIView):
    permission_classes = []

    def post(self, request):
        dataset_file = self.__get_file_from_request(request)
        dataset = self.__load_dataset(dataset_file)
        self.__import_from_dataset(dataset)
        return render(request, "import/success.html")

    def get(self, request):
        return render(request, "import/init.html")

    def __get_file_from_request(self, request: "HttpRequest"):
        return request.FILES["excel_file"].read()

    def __load_dataset(self, dataset_file):
        return tablib.Dataset().load(dataset_file, format="xlsx")
    
    def __import_from_dataset(self, dataset: "tablib.Dataset"):
        # TODO: use django_import_export
        for row in dataset.dict:
            Place.objects.create(
                id=row["PlaceId"],
                code=row["PlaceCode"],
                capacity=row["CapacityBase"],
                rate=row["RateScore"],
                area_size=row["AreasSize"],
            )
