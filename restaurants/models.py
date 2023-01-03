from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=150, blank=True)
    SERVICES = (('Vente à emporter', 'Vente à emporter'),
                ('Livraison', 'Livraison'))
    service1 = models.CharField(max_length=50, choices=SERVICES, blank=True, null=True)
    service2 = models.CharField(max_length=50, choices=SERVICES, blank=True, null=True)
    adresse = models.CharField(max_length=150, blank=False)
    rating = models.FloatField(default=0.0)
    h_open = models.TimeField()
    h_close = models.TimeField()
    image = models.ImageField(upload_to="restaurants", blank=True)
    image_link = models.CharField(default='', max_length=7000000, blank=True)
    num = models.BigIntegerField(blank=True)
    
    def __str__(self):
        return self.name
