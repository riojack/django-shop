import uuid

from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=2048)
    unit_weight = models.CharField(max_length=512)
    count = models.BigIntegerField(default=0)
    upc = models.CharField(max_length=32)
    msrp = models.CharField(max_length=512)

    @classmethod
    def from_json(cls, json_dict):
        return cls.objects.create(
            description=json_dict['description'],
            unit_weight=json_dict['unit_weight'],
            count=json_dict['count'],
            upc=json_dict['upc'],
            msrp=json_dict['msrp']
        )
