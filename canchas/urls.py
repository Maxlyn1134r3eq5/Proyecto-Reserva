from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_canchas, name='listar_canchas'),
    path('nueva/', views.crear_cancha, name='crear_cancha'),
]