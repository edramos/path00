from django.db import models
from general.models import TimeStampedModel

class Enterprise(TimeStampedModel):
    name = models.CharField(max_length=60)
    description = models.TextField(blank=True)
    
    class Meta:
        db_table = "enterprise"