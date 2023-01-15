from django.contrib.auth import get_user_model, login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.forms import ModelForm


def signup_shopper(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        usermail = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")
        if password == password2:
            user = User.objects.create_user(username=username, email=usermail, password=password)
            login(request, user) 
        return redirect('home')

    return render(request, 'accounts/signup.html')

def login_shopper(request):
    if request.method == "POST": 
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('home', foo='bar') 
          
    return render(request,'accounts/forms.html')


def logout_shopper(request):
    logout(request)
    return redirect('home')
