from django.shortcuts import render
from store.models import Product
from rest_framework import viewsets
from store.serializers import PorductSerializer
from rest_framework.permissions import IsAuthenticated

class PorductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = PorductSerializer
    Permission_classes = (IsAuthenticated,)
    filterset_fields = ['id', 'location1']

def index(request):
    products = Product.objects.all()
    
    return render(request, 'store/index.html', context={'products': products})
