from django.contrib import admin
from .models import Pago

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('reserva', 'estado_pago', 'monto', 'metodo_pago', 'fecha_pago')

