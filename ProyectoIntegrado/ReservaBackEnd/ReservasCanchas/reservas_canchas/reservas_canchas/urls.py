"""
URL configuration for reservas_canchas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from usuarios import views as user_views
from canchas import views as cancha_views
from reservas import views as reserva_views

urlpatterns = [
    path('', user_views.login_view, name='login'),
    path('usuarios/home/', user_views.home, name='home'),
    path('logout/', user_views.logout_view, name='logout'),

    # Canchas
    path('canchas/<int:cancha_id>/', cancha_views.detalle_cancha, name='detalle_cancha'),

    # Reservas
    path('reservas/crear/<int:cancha_id>/', reserva_views.crear_reserva, name='crear_reserva'),
    path('reservas/', reserva_views.listar_reservas, name='listar_reservas'),
    path('usuarios/', include('usuarios.urls')),
    path('', include('canchas.urls')),  # Tu home general
]
