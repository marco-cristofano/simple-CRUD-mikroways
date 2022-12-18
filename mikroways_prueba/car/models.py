from django.db import models
from soft_delete.soft_delete import SoftDeleteModel


class Car(SoftDeleteModel):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    year = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name_plural = 'Cars'

    def __str__(self):
        return "%s - %s (%s)" % (self.name, self.brand, self.year)
