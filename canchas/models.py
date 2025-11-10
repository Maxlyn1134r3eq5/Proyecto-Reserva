from django.db import models

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=50)
    precio = models.IntegerField()
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.nombre} - {self.tipo} (${self.precio})"