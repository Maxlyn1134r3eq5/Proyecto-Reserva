from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_reserva_front, name='crear_reserva_front'),
]