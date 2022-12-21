from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, login

User = get_user_model()
# Create your views here.

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.create_user(username=username,password=password)
        login(request, user)
        return redirect('DailyFood:home')

    return render(request, 'accounts/forms.html')
