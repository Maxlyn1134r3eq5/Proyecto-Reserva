from django.contrib import admin
from .models import Reserva

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'cancha', 'fecha_reserva', 'hora_inicio', 'hora_fin', 'estado')


