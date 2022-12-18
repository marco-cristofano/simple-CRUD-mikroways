from django.db import models


class SoftDeleteModelManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(deleted=False)


class SoftDeleteModel(models.Model):
    deleted = models.BooleanField(default=False)
    objects = SoftDeleteModelManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted = True
        self.save()
