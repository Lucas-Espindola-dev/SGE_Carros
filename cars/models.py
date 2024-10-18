from django.db import models
from brands.models import Brand


COLORS = (
    ('RED', 'Red'),
    ('WHITE', 'White'),
    ('GRAY', 'Gray'),
    ('SILVER', 'Silver'),
)


class Car(models.Model):
    model = models.CharField(max_length=250)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='cars')
    factory_year = models.IntegerField()
    model_year = models.IntegerField()
    plate = models.CharField(max_length=10)
    color = models.CharField(max_length=30, choices=COLORS,)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'f {self.model} - {self.color} - {self.model_year} '
