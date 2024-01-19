from django.http import HttpRequest
from django.shortcuts import render
from rest_framework import views

from abc import ABC, abstractmethod


class ImportModelView(views.APIView, ABC):
    def post(self, request):
        dataset_file = self.__read_file_from_request(request)
        dataset = self._load_dataset(dataset_file)
        self._import_from_dataset(dataset)
        return render(request, "import/success.html")

    def get(self, request):
        return render(request, "import/init.html")

    def __read_file_from_request(self, request: "HttpRequest"):
        return request.FILES["excel_file"].read()

    @abstractmethod
    def _load_dataset(self, dataset_file):
        pass

    @abstractmethod
    def _import_from_dataset(self, dataset):
        pass
