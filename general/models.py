from django.db import models

class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    state = models.CharField(max_length=10, default='enabled')
    
    class Meta:
        abstract = True
        

class AddressModel(models.Model):
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    usState = models.CharField(max_length=50)
    zipCode = models.CharField(max_length=10)
    
    class Meta:
        abstract = True
