from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Reserva
from canchas.models import Cancha

@login_required
def listar_reservas(request):
    reservas = Reserva.objects.filter(usuario=request.user)
    return render(request, 'reservas/listar_reservas.html', {'reservas': reservas})

@login_required
def crear_reserva(request, cancha_id):
    cancha = get_object_or_404(Cancha, id=cancha_id)

    if request.method == 'POST':
        fecha = request.POST.get('fecha')
        hora_inicio = request.POST.get('hora_inicio')
        hora_fin = request.POST.get('hora_fin')

        # Verificamos si ya hay una reserva para esa cancha en ese horario
        conflicto = Reserva.objects.filter(
            cancha=cancha,
            fecha=fecha,
            hora_inicio=hora_inicio
        ).exists()

        if conflicto:
            messages.error(request, 'Esta cancha ya está reservada para ese horario.')
            return redirect('crear_reserva', cancha_id=cancha.id)

        Reserva.objects.create(
            usuario=request.user,
            cancha=cancha,
            fecha=fecha,
            hora_inicio=hora_inicio,
            hora_fin=hora_fin,
            estado='Pendiente'
        )
        messages.success(request, 'Reserva creada con éxito.')
        return redirect('listar_reservas')

    return render(request, 'reservas/crear_reserva.html', {'cancha': cancha})

