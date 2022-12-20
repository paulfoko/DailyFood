from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=150, blank=True)
    rating = models.FloatField(default=0.0)
    h_open = models.TimeField()
    h_close = models.TimeField()
    image = models.ImageField(upload_to="restaurants")
    num = models.BigIntegerField(blank=True)
    
    def __str__(self):
        return self.name
