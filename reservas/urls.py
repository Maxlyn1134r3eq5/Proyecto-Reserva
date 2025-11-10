from django.urls import path
from . import views

urlpatterns = [
    path('mis-reservas/', views.listar_reservas, name='listar_reservas'),
    path('crear/', views.crear_reserva, name='crear_reserva'),
    path('modificar/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),
    path('cancelar/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),
]

