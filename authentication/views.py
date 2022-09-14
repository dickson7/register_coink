from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import User


def register(request):
    """view to register a new user.

    Args:
        request (POST)

    Returns:
        The data is evaluated and an error is returned 
        if a field is missing or if the field is already registered in the database. 
        If the registration is successful it redirects to the home page for login. 
    """
    if request.method == "POST":
        context = {'has_error': False, 'data':request.POST}
        email = request.POST.get('email')
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        city = request.POST.get('city')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if len(password)<6:
            messages.add_message(request, messages.ERROR, "La contraseña debe tener al menos 6 caracteres") 
            context['has_error'] = True
        if password != password2:
            messages.add_message(request, messages.ERROR, "Error en la contraseña") 
            context['has_error'] = True
        if not username:
            messages.add_message(request, messages.ERROR, "Se requiere el nombre de usuario") 
            context['has_error'] = True
        if not first_name:
            messages.add_message(request, messages.ERROR, "Se requiere el nombre completo") 
            context['has_error'] = True
        if not city:
            messages.add_message(request, messages.ERROR, "Se requiere la ciudad") 
            context['has_error'] = True
        if User.objects.filter(username=username).exists() :
            messages.add_message(request, messages.ERROR, "El nombre de usuario está ocupado, elige otro") 
            context['has_error'] = True
            return render(request, 'authentication/register.html', context, status=409)
        if User.objects.filter(email=email).exists() :
            messages.add_message(request, messages.ERROR, "El correo electrónico está ocupado, elija otro") 
            context['has_error'] = True
            return render(request, 'authentication/register.html', context, status=409)
        
        if context['has_error']:
            return render(request, 'authentication/register.html', context)
        
        user=User.objects.create_user(username=username,email=email)
        user.set_password(password)
        user.first_name = first_name
        user.city = city
        user.save()
        messages.add_message(request, messages.SUCCESS, "Registro completado con exito")    
        return render(request, 'authentication/login.html', context)
        
    return render(request, 'authentication/register.html')


def login_user(request):
    """View used for login

    Args:
        request (POST)

    """
    if request.method == "POST":
        context = {"data": request.POST}
        username = request.POST.get('username')
        password = request.POST.get('password')

        user=authenticate(request, username=username, password=password)
        
        if not user:
            messages.add_message(request, messages.ERROR, "Credenciales no válidas")
            return render(request, 'authentication/login.html', context, status=401)
        
        login(request, user)
        messages.add_message(request, messages.SUCCESS, f'Bienvenido {user.username}') 
        return redirect(reverse('home'))
        
    return render(request, 'authentication/login.html')

def logout_user(request):
    """View used to log out
    """
    logout(request)

    messages.add_message(request, messages.SUCCESS,
                         'Se ha cerrado la sesión con éxito')

    return redirect(reverse('login'))

