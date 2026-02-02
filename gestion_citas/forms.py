from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Cita,Resena
from django.forms import DateInput, TimeInput


class RegistroUsuarioForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("email", "first_name", "last_name")

    def __init__(self, *args, **kwargs):
        super(RegistroUsuarioForm, self).__init__(*args, **kwargs)
        self.fields["email"].label = "Correo Electrónico"
        self.fields["first_name"].label = "Nombre"
        self.fields["last_name"].label = "Apellido"


class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ["barbero", "servicio", "fecha", "hora", "notas"]
        widgets = {
            "fecha": DateInput(attrs={"type": "date", "class": "form-control"}),
            "hora": TimeInput(attrs={"type": "time", "class": "form-control"}),
            "notas": forms.Textarea(
                attrs={
                    "rows": 3,
                    "class": "form-control",
                    "placeholder": "Ej: Corte con navaja...",
                }
            ),
            "barbero": forms.Select(attrs={"class": "form-select"}),
            "servicio": forms.Select(attrs={"class": "form-select"}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data["fecha"]
        import datetime

        if fecha < datetime.date.today():
            raise forms.ValidationError("No puedes reservar en una fecha pasada.")
        return fecha


class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ["first_name", "last_name", "email"]


class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ["puntuacion", "comentario"]
        widgets = {
            "puntuacion": forms.Select(attrs={"class": "form-select"}),
            "comentario": forms.Textarea(
                attrs={
                    "rows": 4,
                    "class": "form-control",
                    "placeholder": "¿Qué tal fue el servicio?",
                }
            ),
        }
        labels = {
            "puntuacion": "Puntuación (1-5 Estrellas)",
            "comentario": "Tu opinión",
        }
