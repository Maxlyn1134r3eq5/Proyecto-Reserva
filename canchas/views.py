from django.shortcuts import render, redirect
from .models import Cancha

def listar_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'canchas/listar_canchas.html', {'canchas': canchas})

def crear_cancha(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        precio = request.POST['precio']
        Cancha.objects.create(nombre=nombre, precio=precio)
        return redirect('listar_canchas')
    return render(request, 'canchas/crear.html')

