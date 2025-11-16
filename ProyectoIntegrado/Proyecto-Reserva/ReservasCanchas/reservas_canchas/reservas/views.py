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

from django.shortcuts import render

def crear_reserva_front(request):
    canchas = Cancha.objects.all()
    return render(request, 'reservas/formulario_reserva.html', {'canchas': canchas})

from django.http import JsonResponse

def horas_disponibles(request):
    cancha_id = request.GET.get("cancha")
    fecha = request.GET.get("fecha")

    reservas = Reserva.objects.filter(cancha_id=cancha_id, fecha=fecha)

    horas_ocupadas = reservas.values_list("hora_inicio", flat=True)

    HORAS_TOTALES = [
        "08:00", "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00", "15:00",
        "16:00", "17:00", "18:00", "19:00",
        "20:00", "21:00", "22:00",
    ]

    disponibles = [h for h in HORAS_TOTALES if h not in horas_ocupadas]

    return JsonResponse({"horas": disponibles})

from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def guardar_reserva(request):

    if request.method == "POST":

        Reserva.objects.create(
            usuario=request.user,
            cancha_id=request.POST["cancha"],
            fecha=request.POST["fecha"],
            hora_inicio=request.POST["hora_inicio"],
            hora_fin=request.POST["hora_fin"],
            cantidad_jugadores=request.POST["cantidad_jugadores"],
            estado="Pendiente"
        )

        messages.success(request, "Reserva creada correctamente")
        return redirect("listar_reservas")
