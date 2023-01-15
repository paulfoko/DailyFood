from django.db import models

from restaurants.models import Restaurant
from supermarcher.models import SuperMarket

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date_added']
        
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="products", blank=True)
    image_link = models.CharField(default='', max_length=7000000, blank=True)
    stock = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    rating = models.FloatField(default=0.0)
    description = models.TextField(max_length=1500, blank=True)
    date_add = models.DateTimeField(auto_now=True)
    location = models.ForeignKey(Restaurant, related_name='source', on_delete=models.CASCADE, null=True, blank=True)
    Category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    class Meta:
        ordering = ['-date_add']
        
    def __str__(self):
        return self.name
        
class Articles(models.Model):
    product = models.ForeignKey(Product, related_name='articles', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name

class Shopp_Cart(models.Model):
    date_created = models.DateTimeField(auto_now=True)
    article = models.ManyToManyField(Articles)
    quantite = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateField(blank=True, null=True)


    
    def __str__(self):
        return self.name



