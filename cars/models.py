from django.db import models
from brands.models import Brand


class Car(models.Model):
    model = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10)
    color = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
