from django.shortcuts import render, redirect
from restaurants.models import Restaurant
from django.forms import ModelForm
from django.contrib.auth.models import User
from restaurants.models import Restaurant
from django.contrib import messages

def restaurant(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/index.html', context={'restaurants': restaurants})

class RetoForm(ModelForm):
    class Meta:
        model = User
        fields = ('username','last_name','first_name','email', 'password')

class ProfilRetoForm(ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"
        
        
def sign_resto(request):
    reto_form = RetoForm()
    reto_form2 = ProfilRetoForm()
    if request.method == "POST":
        form = RetoForm(request.POST)
        if form.is_valid():
            new_resto = form.save()
            messages.success(request,'Nouveau contact '+new_resto.username)
            context = {'resto': new_resto}
            return redirect('resto')
        context = {'form': form}
    return render(request,'restaurants/inscription.html', {'reto_form' : reto_form})

def resto(request):
    return render(request, 'restaurants/restaurant.html',)

def join_us(request):
    return render(request,'join_us.html')
