from django.db import models
from django.contrib.auth.models import User 
from django.core.exceptions import ValidationError 
from datetime import timedelta, datetime

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos") 

    def __str__(self):
        return f"{self.nombre} ({self.duracion} min) - {self.precio}€"

class Barbero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='barberos/', blank=True, null=True)
    experiencia = models.PositiveIntegerField(help_text="Años de experiencia")
    
    especialidades = models.ManyToManyField(Servicio, related_name='barberos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Cita(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    notas = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['fecha', 'hora']

    def __str__(self):
        return f"Cita de {self.usuario.username} con {self.barbero.nombre} el {self.fecha}"

    def clean(self):
        cita_existente = Cita.objects.filter(
            barbero=self.barbero,
            fecha=self.fecha,
            hora=self.hora
        ).exclude(id=self.id)

        if cita_existente.exists():
            raise ValidationError(f"El barbero {self.barbero.nombre} ya tiene una cita a esa hora.")
            
        cita_datetime = datetime.combine(self.fecha, self.hora)
        if cita_datetime < datetime.now():
             raise ValidationError("No puedes reservar una cita en el pasado.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)