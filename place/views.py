from django.shortcuts import render

# Create your views here.
from .models import Place
import tablib

# TODO: use django_import_export
def import_from_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['excel_file']
        dataset = tablib.import_set(excel_file)
        for row in dataset.dict:
            Place.objects.create(id=row['PlaceId'],
                                  code=row['PlaceCode'],
                                  capacity=row['CapacityBase'],
                                  rate=row['RateScore'],
                                  area_size=row['AreasSize'])

        return render(request, 'import_success.html')

    return render(request, 'import_form.html')