from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    correo = models.EmailField(unique=True)
    num_celular = models.CharField(max_length=15, blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    rol = models.CharField(
        max_length=20,
        choices=[('admin', 'Administrador'), ('cliente', 'Cliente')],
        default='cliente'
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return self.username


