from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Usuario

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        correo = request.POST['correo']
        password = request.POST['password']

        if Usuario.objects.filter(username=username).exists():
            messages.error(request, 'Ese nombre de usuario ya existe.')
            return redirect('register')

        usuario = Usuario.objects.create_user(
            username=username,
            email=correo,
            password=password
        )
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'usuarios/register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('usuarios:home')
        else:
            messages.error(request, 'Credenciales incorrectas.')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('usuarios:login')

@login_required
def home(request):
    from canchas.models import Cancha
    canchas = Cancha.objects.all()
    return render(request, 'usuarios/home.html', {'canchas': canchas})

