from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reserva, Cancha
from datetime import datetime

# 🔹 Listar reservas del usuario autenticado
@login_required
def listar_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})


# 🔹 Crear una nueva reserva
@login_required
def crear_reserva(request):
    canchas = Cancha.objects.all()

    if request.method == 'POST':
        cancha_id = request.POST['cancha']
        fecha = request.POST['fecha']
        hora_inicio = request.POST['hora_inicio']
        hora_fin = request.POST['hora_fin']
        cantidad_jugadores = request.POST['cantidad_jugadores']

        cancha = get_object_or_404(Cancha, id=cancha_id)

        # Validación básica: que no haya otra reserva para esa cancha y horario
        reservas_existentes = Reserva.objects.filter(
            cancha=cancha,
            fecha=fecha,
            hora_inicio=hora_inicio
        )
        if reservas_existentes.exists():
            messages.error(request, 'Esa cancha ya está reservada en ese horario.')
            return redirect('crear_reserva')

        reserva = Reserva.objects.create(
            usuario=request.user,
            cancha=cancha,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            cantidad_jugadores=cantidad_jugadores,
            estado='Pendiente'
        )
        reserva.save()
        messages.success(request, 'Reserva creada correctamente.')
        return redirect('listar_reservas')

    return render(request, 'reservas/crear_reserva.html', {'canchas': canchas})


# 🔹 Modificar una reserva
@login_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    canchas = Cancha.objects.all()

    if request.method == 'POST':
        reserva.cancha_id = request.POST['cancha']
        reserva.fecha = request.POST['fecha']
        reserva.hora_inicio = request.POST['hora_inicio']
        reserva.hora_fin = request.POST['hora_fin']
        reserva.cantidad_jugadores = request.POST['cantidad_jugadores']
        reserva.save()
        messages.success(request, 'Reserva modificada correctamente.')
        return redirect('listar_reservas')

    return render(request, 'reservas/modificar_reserva.html', {'reserva': reserva, 'canchas': canchas})


# 🔹 Cancelar una reserva
@login_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id, usuario=request.user)
    reserva.estado = 'Cancelada'
    reserva.save()
    messages.info(request, 'Reserva cancelada correctamente.')
    return redirect('listar_reservas')


