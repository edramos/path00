from django.db import models
from locations.models import Location
from general.models import TimeStampedModel, AddressModel


class User(TimeStampedModel):
    location = models.OneToOneField(Location, on_delete=models.CASCADE,)
    
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    
    class Meta:
        db_table = "user"


class Profile(TimeStampedModel, AddressModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,)
    
    firstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    telephone = models.CharField(max_length=20, blank=True)
    role = models.CharField(max_length=20)
    
    class Meta:
        db_table = "profile"
