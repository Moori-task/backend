from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Place(models.Model):
    id = models.CharField(
        max_length=24,
        unique=True,
    )

    code = models.PositiveIntegerField(
        primary_key=True
    )

    capacity = models.PositiveIntegerField()

    rate = models.FloatField(validators=[
        MinValueValidator(0.0),
        MaxValueValidator(5.0)
    ])

    area_size = models.PositiveIntegerField()

