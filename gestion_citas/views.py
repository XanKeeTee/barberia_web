from collections import defaultdict
from django.forms import ValidationError
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EditarPerfilForm, RegistroUsuarioForm, CitaForm, ResenaForm,CitaStaffForm
from .models import Servicio, Barbero, Cita, Resena
from datetime import date, datetime
from django.db.models import Count
import json


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
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            # ... (código de guardado igual que antes) ...
            cita = form.save(commit=False)
            cita.usuario = request.user
            try:
                cita.full_clean()
                cita.save()
                messages.success(request, '¡Cita reservada con éxito!')
                return redirect('mis_citas')
            except ValidationError as e:
                form.add_error(None, e)
    else:
        form = CitaForm()
    
    # --- DATOS PARA JAVASCRIPT Y DISEÑO ---
    barberos = Barbero.objects.all()
    servicios = Servicio.objects.all()
    
    # 1. Definimos los huecos (Ahora con medias horas)
    # Puedes ajustar esto a tu horario real
    horarios_disponibles = [
        "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30",
        "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30"
    ]

    # 2. Obtenemos citas futuras ocupadas
    citas_futuras = Cita.objects.filter(fecha__gte=date.today())
    agenda_ocupada = defaultdict(lambda: defaultdict(list))
    
    for cita in citas_futuras:
        fecha_str = cita.fecha.strftime("%Y-%m-%d")
        # Aseguramos formato HH:MM (sin segundos)
        hora_str = cita.hora.strftime("%H:%M") 
        agenda_ocupada[cita.barbero.id][fecha_str].append(hora_str)

    # Convertimos a JSON
    agenda_ocupada_json = json.dumps({k: dict(v) for k, v in agenda_ocupada.items()})
    precios_json = json.dumps({s.id: float(s.precio) for s in servicios})
    
    return render(request, 'gestion_citas/citas/reservar_cita.html', {
        'form': form,
        'barberos': barberos,
        'servicios': servicios,
        'agenda_json': agenda_ocupada_json,
        'precios_json': precios_json,
        'horarios': horarios_disponibles, # <--- PASAMOS LA LISTA DE HORAS
    })


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
@login_required
def agenda_profesional(request):
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para acceder a la agenda profesional.")
        return redirect('home')

    Cita.objects.filter(fecha__lt=date.today(), estado='PENDIENTE').update(estado='CANCELADA')

    ahora_mismo = datetime.now().time()
    Cita.objects.filter(fecha=date.today(), hora__lt=ahora_mismo, estado='PENDIENTE').update(estado='CANCELADA')

    hoy = date.today()
    citas = Cita.objects.filter(fecha__gte=hoy).order_by('fecha', 'hora')
    
    return render(request, 'gestion_citas/citas/agenda_profesional.html', {
        'citas': citas,
        'hoy': hoy
    })


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


@login_required
def mi_perfil(request):
    usuario = request.user
    if request.method == "POST":
        form = EditarPerfilForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, "Tus datos han sido actualizados.")
            return redirect("mi_perfil")
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, "gestion_citas/auth/perfil.html", {"form": form})


@login_required
def dashboard_staff(request):
    if not request.user.is_staff:
        return redirect("home")

    # 1. Datos para la Gráfica: Citas por Barbero
    # Esto crea una lista: [{'barbero__nombre': 'Juan', 'total': 5}, ...]
    datos_barberos = Cita.objects.values("barbero__nombre").annotate(total=Count("id"))

    # Preparamos las listas para JavaScript
    nombres = [d["barbero__nombre"] for d in datos_barberos]
    cantidades = [d["total"] for d in datos_barberos]

    # 2. Datos simples (KPIs)
    total_citas = Cita.objects.count()
    ingresos_estimados = sum([c.servicio.precio for c in Cita.objects.all()])

    return render(
        request,
        "gestion_citas/citas/dashboard.html",
        {
            "nombres_js": nombres,
            "cantidades_js": cantidades,
            "total_citas": total_citas,
            "ingresos": ingresos_estimados,
        },
    )


@login_required
def dejar_resena(request, barbero_id):
    barbero = get_object_or_404(Barbero, id=barbero_id)

    if request.method == "POST":
        form = ResenaForm(request.POST)
        if form.is_valid():
            resena = form.save(commit=False)
            resena.usuario = request.user  # Usuario actual
            resena.barbero = barbero  # Barbero seleccionado
            resena.save()
            messages.success(request, f"¡Gracias! Has valorado a {barbero.nombre}.")
            return redirect("home")  # O volver a mis_citas
    else:
        form = ResenaForm()

    return render(
        request,
        "gestion_citas/citas/dejar_resena.html",
        {"form": form, "barbero": barbero},
    )

@login_required
def editar_cita_staff(request, cita_id):
    # Seguridad: Solo staff puede entrar aquí
    if not request.user.is_staff:
        messages.error(request, "No tienes permisos para realizar esta acción.")
        return redirect('home')

    cita = get_object_or_404(Cita, id=cita_id)

    if request.method == 'POST':
        form = CitaStaffForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cita actualizada correctamente.')
            return redirect('agenda_profesional') # Vuelve a la agenda
    else:
        form = CitaStaffForm(instance=cita)

    return render(request, 'gestion_citas/citas/editar_cita_staff.html', {
        'form': form,
        'cita': cita
    })  