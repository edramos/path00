from django.db import models
from general.models import AddressModel, TimeStampedModel
from enterprises.models import Enterprise

class Location(AddressModel, TimeStampedModel):
    enterprise = models.ForeignKey(Enterprise, on_delete=models.CASCADE)
    
    name = models.CharField(max_length=60)
    telephone = models.CharField(max_length=20, blank=True)
    lat = models.FloatField()
    lng = models.FloatField()
    
    class Meta:
        db_table = "location"