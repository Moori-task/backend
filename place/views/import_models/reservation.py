import tablib

from place.models.reservation import ReserveSlot
from .abstract import ImportModelView


class ImportReservationView(ImportModelView):
    permission_classes = []

    def _load_dataset(self, dataset_file):
        dataset_file = dataset_file.decode("utf-8")
        return tablib.Dataset().load(dataset_file, format="csv")

    def _import_from_dataset(self, dataset: "tablib.Dataset"):
        # TODO: use django_import_export
        for row in dataset.dict:
            ReserveSlot.objects.create(
                place_id=row["acc_code"],
                date=row["DateEn"].replace("/", "-"),
                status=row["Status"],
            )
