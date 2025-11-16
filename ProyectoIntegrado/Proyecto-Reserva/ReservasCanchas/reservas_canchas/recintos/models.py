from django.db import models
from ubicaciones.models import Ubicacion
from usuarios.models import Usuario

class Recinto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    horario = models.CharField(max_length=100)
    ubicacion = models.ForeignKey(Ubicacion, on_delete=models.CASCADE)
    administrador = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'admin'})

    def __str__(self):
        return self.nombre

