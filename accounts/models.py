from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField


class Shopper(models.Model):
    SEX = (('H', 'Homme'),
           ('F', 'Femme'))
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField(null=False)
    phone = PhoneField(blank=False, null=False, help_text='Contact phone number')
    sex = models.CharField(max_length=1, choices=SEX, default='H')
    ville = models.CharField(max_length=50)
    Quartier = models.CharField(max_length=75)
    
