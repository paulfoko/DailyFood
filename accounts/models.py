
from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField


class Shopper(AbstractUser):
    SEX = ( ('H','Homme'),
            ('F','Femme'))
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    sex = models.CharField(max_length=1, choices=SEX, default='H')
    birth_date = models.DateField(blank=True, null=True)
