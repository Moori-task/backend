from django.db import models


class ReserveSlot(models.Model):
    place = models.ForeignKey(
        to="place.Place", related_name="reserve_slots", on_delete=models.CASCADE
    )

    date = models.DateField()

    class ReserveSlotStatus(models.TextChoices):
        available = "available"
        reserved = "reserved"

    status = models.CharField(choices=ReserveSlotStatus.choices)
