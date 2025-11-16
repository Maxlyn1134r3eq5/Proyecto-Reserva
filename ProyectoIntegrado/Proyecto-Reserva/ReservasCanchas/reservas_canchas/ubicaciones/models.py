from django.db import models

class Ubicacion(models.Model):
    nombre = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    comuna = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} - {self.ciudad}"

