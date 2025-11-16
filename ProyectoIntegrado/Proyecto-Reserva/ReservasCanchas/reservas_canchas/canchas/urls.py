from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_canchas, name='home'),  # o la vista que tengas como home
    path('<int:cancha_id>/', views.detalle_cancha, name='detalle_cancha'),
]
