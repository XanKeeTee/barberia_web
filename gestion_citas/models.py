from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.exceptions import ValidationError
from datetime import datetime

# 1. GESTOR DE USUARIOS PERSONALIZADO (Esto arregla el error de createsuperuser)
class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('El superusuario debe tener is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('El superusuario debe tener is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

# 2. MODELO DE USUARIO (Login con Email)
class Usuario(AbstractUser):
    username = None 
    email = models.EmailField('Correo Electrónico', unique=True)
    first_name = models.CharField('Nombre', max_length=150)
    last_name = models.CharField('Apellido', max_length=150)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    # Conectamos el gestor nuevo aquí:
    objects = UsuarioManager()

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"

# 3. MODELO SERVICIO
class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos") 

    def __str__(self):
        return f"{self.nombre} - {self.precio}€"

# 4. MODELO BARBERO
class Barbero(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='barberos/', blank=True, null=True)
    experiencia = models.PositiveIntegerField(help_text="Años de experiencia")
    especialidades = models.ManyToManyField(Servicio, related_name='barberos')

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# 5. MODELO CITA
class Cita(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='citas')
    barbero = models.ForeignKey(Barbero, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    notas = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['fecha', 'hora']

    def clean(self):
        cita_existente = Cita.objects.filter(
            barbero=self.barbero,
            fecha=self.fecha,
            hora=self.hora
        ).exclude(id=self.id)

        if cita_existente.exists():
            raise ValidationError(f"El barbero {self.barbero.nombre} ya tiene una cita a esa hora.")
            
        # Validación: evitar fechas pasadas, etc. se puede añadir aquí
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)