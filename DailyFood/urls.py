"""DailyFood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from store.views import index,cart
from restaurants.views import restaurant
from accounts.views import login_shopper, signup_shopper
from DailyFood import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name='home'),
    path('Dailyfood.cm/restaurants/', restaurant, name='restaurants'),
    path('Dailyfood.cm/signup/', signup_shopper, name='Signup'),
    path('Dailyfood.cm/login/', login_shopper, name='Login'),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
