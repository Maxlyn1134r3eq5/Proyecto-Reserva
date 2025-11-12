from django.db import models
from reservas.models import Reserva

class Pago(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    estado_pago = models.CharField(max_length=20)
    monto = models.PositiveIntegerField()
    metodo_pago = models.CharField(max_length=50)
    fecha_pago = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pago {self.id} - {self.estado_pago}"

