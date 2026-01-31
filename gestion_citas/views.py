from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegistroUsuarioForm, CitaForm
from .models import Servicio, Barbero, Cita
from datetime import date


def home(request):
    servicios = Servicio.objects.all()
    barberos = Barbero.objects.all()
    return render(
        request,
        "gestion_citas/public/home.html",
        {
            "servicios": servicios,
            "barberos": barberos,
        },
    )


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            login(request, usuario)
            messages.success(request, "Registro completado")
            return redirect("home")
    else:
        form = RegistroUsuarioForm()
    return render(request, "gestion_citas/auth/registro.html", {"form": form})


@login_required
def mis_citas(request):
    citas = Cita.objects.filter(usuario=request.user).order_by("-fecha", "-hora")
    return render(request, "gestion_citas/citas/mis_citas.html", {"citas": citas})


@login_required
def reservar_cita(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        if form.is_valid():
            cita = form.save(commit=False)
            cita.usuario = request.user
            try:
                cita.full_clean()
                cita.save()
                messages.success(request, "¡Cita reservada con éxito!")
                return redirect("mis_citas")
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CitaForm()

    return render(request, "gestion_citas/citas/reservar_cita.html", {"form": form})


@login_required
def cancelar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, usuario=request.user)

    if request.method == "POST":
        cita.delete()
        messages.warning(request, "La cita ha sido cancelada.")
        return redirect("mis_citas")

    return render(
        request, "gestion_citas/citas/confirmar_cancelar.html", {"cita": cita}
    )


@login_required
def agenda_profesional(request):
    if not request.user.is_staff:
        messages.error(
            request, "No tienes permisos para acceder a la agenda profesional."
        )
        return redirect("home")

    hoy = date.today()

    citas = Cita.objects.filter(fecha__gte=hoy).order_by("fecha", "hora")

    return render(
        request,
        "gestion_citas/citas/agenda_profesional.html",
        {"citas": citas, "hoy": hoy},
    )


@login_required
def editar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id, usuario=request.user)

    if request.method == "POST":
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "La cita ha sido modificada correctamente.")
                return redirect("mis_citas")
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CitaForm(instance=cita)

    return render(
        request, "gestion_citas/citas/editar_cita.html", {"form": form, "cita": cita}
    )


def error_404(request, exception):
    return render(request, "gestion_citas/public/404.html", status=404)
