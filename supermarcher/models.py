from django.db import models

class SuperMarket(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=150, blank=True)
    rating = models.FloatField(default=0.0)
    h_open = models.TimeField()
    h_close = models.TimeField()
    image = models.ImageField(upload_to="restaurants")
    
    def __str__(self):
        return self.name
    