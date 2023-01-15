from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=150, blank=True)
    services = models.CharField(max_length=250, blank=False, null=False)
    adresse = models.CharField(max_length=150, blank=False)
    rating = models.FloatField(default=0.0)
    h_open = models.TimeField()
    h_close = models.TimeField()
    image = models.ImageField(upload_to="restaurants", blank=True)
    image_link = models.CharField(default='', max_length=7000000, blank=True)
    num = models.BigIntegerField(blank=True)
    
    def __str__(self):
        return self.name
