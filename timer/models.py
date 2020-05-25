from django.db import models
from django.conf import settings
from django.utils import timezone
import datetime
from datetime import date

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    time=models.DateField()
    #time_until_event=time.-datetime.date.today()
    published_date=models.DateField(blank=True, null=True)
    
    def publish(self):
        published_date=datetime.date.today()
        self.save()
    def __str__(self):
        return self.name
