from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Servicio, Barbero


def home(request):
    servicios = Servicio.objects.all()
    barberos = Barbero.objects.all()
    return render(request, 'gestion_citas/public/home.html', {
        'servicios': servicios,
        'barberos': barberos,
    })

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, f'¡Bienvenido, {usuario.username}! Tu cuenta ha sido creada.')
            return redirect('home')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = UserCreationForm()

    return render(request, 'gestion_citas/auth/registro.html', {'form': form})