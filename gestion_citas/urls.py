from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    # --- Rutas de Autenticación ---
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(
        template_name='gestion_citas/auth/login.html',
        redirect_authenticated_user=True
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('mis-citas/', views.mis_citas, name='mis_citas'),
    path('reservar/', views.reservar_cita, name='reservar_cita'),
    path('editar/<int:cita_id>/', views.editar_cita, name='editar_cita'),
    path('cancelar/<int:cita_id>/', views.cancelar_cita, name='cancelar_cita'),
    path('agenda-staff/', views.agenda_profesional, name='agenda_profesional'),
]

handler404 = 'gestion_citas.views.error_404'