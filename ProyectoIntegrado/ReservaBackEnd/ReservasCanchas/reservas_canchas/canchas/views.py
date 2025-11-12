from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Cancha

def listar_canchas(request):
    canchas = Cancha.objects.all()
    return render(request, 'canchas/listar_canchas.html', {'canchas': canchas})

@login_required
def detalle_cancha(request, cancha_id):
    cancha = get_object_or_404(Cancha, id=cancha_id)
    return render(request, 'canchas/detalle_cancha.html', {'cancha': cancha})
