from django.shortcuts import render
from restaurants.models import Restaurant

def restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', context={'restaurants': restaurants})
