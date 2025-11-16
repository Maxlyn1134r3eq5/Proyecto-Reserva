from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    rol = models.CharField(
        max_length=20,
        choices=[('admin', 'Administrador'), ('cliente', 'Cliente')],
        default='cliente'
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='usuario_groups',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='usuario_permissions',
        blank=True
    )

    def __str__(self):
        return self.username
