from django.db import models
from usuarios.models import Usuario
from canchas.models import Cancha

class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    cantidad_jugadores = models.PositiveIntegerField(default=0)  # ✅ Campo agregado
    estado = models.CharField(max_length=20, default='Pendiente')

    def __str__(self):
        return f"Reserva de {self.usuario} en {self.cancha} - {self.fecha}"

