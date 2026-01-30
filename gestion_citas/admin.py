from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario, Servicio, Barbero, Cita

# Configuración para gestionar el Usuario personalizado en el Admin
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    # Esto es necesario porque ya no usamos username
    ordering = ['email']

admin.site.register(Servicio)
admin.site.register(Barbero)

@admin.register(Cita)
class CitaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'barbero', 'servicio', 'fecha', 'hora', 'estado')
    list_filter = ('fecha', 'estado', 'barbero')