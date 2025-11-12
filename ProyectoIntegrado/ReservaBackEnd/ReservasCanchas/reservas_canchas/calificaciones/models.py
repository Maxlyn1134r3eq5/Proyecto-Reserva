from django.db import models
from usuarios.models import Usuario
from canchas.models import Cancha

class Calificacion(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    cancha = models.ForeignKey(Cancha, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    puntaje = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.cancha.nombre} ({self.puntaje})"

