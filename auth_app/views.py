# from django.shortcuts import render, redirect
# from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from django.contrib.auth import login, logout
# from .middlewares import auth, guest

# @guest
# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request,user)
#             return redirect('dashboard')
#     else:
#         initial_data = {'username':'', 'password1':'', 'password2':''}
#         form = UserCreationForm(initial=initial_data)
#     return render(request, 'auth/register.html', {'form':form})  

# @guest      
# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request ,data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             login(request,user)
#             return redirect('dashboard')
#     else:
#         initial_data = {'username':'', 'password':''}
#         form = AuthenticationForm(initial=initial_data)
#     return render(request, 'auth/login.html', {'form':form}) 

# def logout_view(request):
#     logout(request)
#     return redirect('login')

# @auth
# def dashboard_view(request):
#     return render(request, 'dashboard.html')






from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from .middlewares import auth, guest
from .models import CustomUser
from .forms import CustomUserCreationForm 
from django.contrib import messages
from django.contrib.auth import get_user_model, login as auth_login
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm

User = get_user_model()

@guest
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'auth/register.html', {'form': form})

@guest
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@auth
def dashboard_view(request):
    return render(request, 'dashboard.html')