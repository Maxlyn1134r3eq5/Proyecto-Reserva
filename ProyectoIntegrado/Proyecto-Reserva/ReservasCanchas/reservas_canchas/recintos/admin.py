from django.contrib import admin
from .models import Recinto

@admin.register(Recinto)
class RecintoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'horario', 'ubicacion', 'administrador')

