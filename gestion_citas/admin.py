from django.contrib import admin
from .models import Servicio, Barbero, Cita

class CitaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'barbero', 'servicio', 'fecha', 'hora', 'estado')
    list_filter = ('fecha', 'estado', 'barbero')
    search_fields = ('usuario__username', 'barbero__nombre') 

admin.site.register(Servicio)
admin.site.register(Barbero)
admin.site.register(Cita, CitaAdmin)