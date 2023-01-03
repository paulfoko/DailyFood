from store.models import Product
from rest_framework import serializers
    
class PorductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = 'name', 'image', 'image_link', 'price', 'stock'
        