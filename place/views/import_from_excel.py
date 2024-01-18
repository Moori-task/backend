from django.shortcuts import render
from rest_framework import views
# Create your views here.
from place.models import Place
import tablib

class ImportFromExcel(views.APIView):
    def post(self, request):
        excel_file = request.FILES['excel_file']
        dataset = tablib.import_set(excel_file)
        # TODO: use django_import_export
        for row in dataset.dict:
            Place.objects.create(id=row['PlaceId'],
                                  code=row['PlaceCode'],
                                  capacity=row['CapacityBase'],
                                  rate=row['RateScore'],
                                  area_size=row['AreasSize'])

        return render(request, 'import/success.html')

    def get(self, request):
        return render(request, 'import/init.html')      

    