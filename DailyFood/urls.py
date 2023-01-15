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
from django.urls import path, include
from store.views import index
from restaurants.views import restaurant, join_us, sign_resto, resto
from accounts.views import login_shopper, signup_shopper
from DailyFood import settings
from django.conf.urls.static import static
from store.urls import router as router_produit
from rest_framework import routers

router = routers.DefaultRouter()
router.registry.extend(router_produit.registry) 
urlpatterns = [
                  path('', index, name='home'),
                  path('api/', include(router.urls)),
                  path('restaurants/', restaurant, name='restaurants'),
                  path('join_us/', join_us, name='join_us'),
                  path('administration/inscription', sign_resto, name='sign_resto'),
                  path('administration/restaurant', resto, name='resto'),
                  path('signup/', signup_shopper, name='Signup'),
                  path('login/', login_shopper, name='Login'),
                  path('admin/', admin.site.urls)
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
