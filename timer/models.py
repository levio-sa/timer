from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=100)
    time=models.DateField()
    time_until_event=models.DateField(auto_now=True)
    published_date=models.DateField()
    
    def publish(self):
        
        self.save()
    def __str__(self):
        return self.name
