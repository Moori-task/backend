# Create your views here.
from place.models import Place
import tablib

from .abstract import ImportModelView


class ImportPlaceView(ImportModelView):
    permission_classes = []

    def _load_dataset(self, dataset_file):
        return tablib.Dataset().load(dataset_file, format="xlsx")

    def _import_from_dataset(self, dataset: "tablib.Dataset"):
        # TODO: use django_import_export
        for row in dataset.dict:
            Place.objects.create(
                id=row["PlaceId"],
                code=row["PlaceCode"],
                capacity=row["CapacityBase"],
                rate=row["RateScore"],
                area_size=row["AreasSize"],
            )
