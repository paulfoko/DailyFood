from django.shortcuts import render, get_object_or_404
from store.models import Product, Shopp_Cart


# Create your views here.
def index(request):
    products = Product.objects.all()
    
    return render(request, 'store/index.html', context={'products': products})

def cart(request, id):
    products = Product.objects.all()
    
    return render(request, 'store/cart.html', context={'products': products})