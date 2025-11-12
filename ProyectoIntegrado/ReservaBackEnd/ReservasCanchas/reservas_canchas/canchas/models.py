from django.db import models
from recintos.models import Recinto

class Cancha(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.PositiveIntegerField()
    recinto = models.ForeignKey(Recinto, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} - {self.recinto.nombre}"

