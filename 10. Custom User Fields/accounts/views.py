from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from .forms import RegistrationForm
# Create your views here.

def RegisterView(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
        
    else:
        form = RegistrationForm()
    
    return render(request, 'accounts/register.html', {'form':form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login (request, user)
            return redirect('matrimony:profile_list')
        
    else:
        form = AuthenticationForm()
    
    return render(request, 'accounts/login.html', {'form':form})

def LogoutView(request):
    logout(request)
    return redirect('accounts:login')