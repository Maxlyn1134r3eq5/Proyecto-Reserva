from django.contrib import admin
from .models import Cancha

@admin.register(Cancha)
class CanchaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'recinto')

