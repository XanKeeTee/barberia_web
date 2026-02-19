💈 BarberiaWeb - Sistema de Reservas para Barberías
=====================================================

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) ![Bootstrap](https://img.shields.io/badge/Bootstrap_5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

BarberiaWeb es una aplicación web integral desarrollada para la digitalización y automatización de citas en barberías y peluquerías. Diseñada para mejorar la experiencia del cliente y optimizar el tiempo de los profesionales, eliminando la gestión telefónica tradicional.

🚀 Características Principales
------------------------------

### Para el Cliente

*   **Reserva de Citas Inteligente:** Sistema de reservas paso a paso (Servicio > Profesional > Fecha > Hora).
*   **Catálogo Visual:** Galería de servicios y estilos integrados en la plataforma.
*   **Horarios Dinámicos:** El sistema diferencia automáticamente los horarios entre semana y los fines de semana (ej. Sábados solo mañanas), adaptando la disponibilidad en tiempo real.
*   **Control de Disponibilidad:** Bloqueo automático de horas ya reservadas o pasadas en el día actual.

### Para la Administración (Barberos/Gerencia)

*   **Panel de Control:** Gestión completa a través del panel de administración de Django.
*   **Gestión de Personal:** Creación y edición de perfiles de barberos.
*   **Gestión de Servicios:** Control de precios, duración y catálogo de cortes.
*   **Control de Agenda:** Visualización en tiempo real de las citas diarias.

🛠️ Stack Tecnológico
---------------------

*   **Backend:** Python 3.11+ / Django 5.x
*   **Frontend:** HTML5, CSS3, JavaScript Vanilla
*   **Framework UI:** Bootstrap 5
*   **Librerías Adicionales:** Flatpickr (Calendario interactivo)
*   **Base de Datos:** SQLite (Desarrollo) / PostgreSQL (Preparado para Producción)

⚙️ Instalación y Despliegue Local
---------------------------------

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1\. Clonar el repositorio

    git clone https://github.com/tu-usuario/barberia_web.git
    cd barberia_web

### 2\. Crear y activar el entorno virtual

En Windows:

    python -m venv env
    .\env\Scripts\activate

En macOS / Linux:

    python3 -m venv env
    source env/bin/activate

### 3\. Instalar dependencias

    pip install -r requirements.txt

### 4\. Configurar la Base de Datos (Migraciones)

    python manage.py makemigrations
    python manage.py migrate

### 5\. Crear el superusuario (Administrador)

    python manage.py createsuperuser

_(Sigue las instrucciones en pantalla para configurar email y contraseña)._

### 6\. Ejecutar el servidor de desarrollo

    python manage.py runserver

La aplicación estará disponible en: `http://127.0.0.1:8000/`  
El panel de administración en: `http://127.0.0.1:8000/admin/`

📂 Estructura del Proyecto
--------------------------

    barber_gestion/
      ├── manage.py
      ├── core/                   # Configuración principal de Django
      ├── gestion_citas/          # Aplicación principal
      │   ├── models.py           # Modelos de base de datos (Barbero, Servicio, Cita)
      │   ├── views.py            # Lógica de negocio y controladores
      │   ├── urls.py             # Rutas de la aplicación
      │   ├── templates/          # Plantillas HTML (incluye lógica JS dinámica)
      │   └── static/             # Archivos CSS, JS e imágenes estáticas
      └── db.sqlite3              # Base de datos local

📝 Próximas Implementaciones (Roadmap)
--------------------------------------

*    Integración de pasarela de pago (Stripe/PayPal) para reservas con fianza.
*    Envío automático de recordatorios por WhatsApp o Correo Electrónico.
*    Panel estadístico (Dashboard) de ingresos y citas mensuales para el administrador.

📄 Licencia
-----------

Este proyecto es parte de un entorno educativo para el ciclo de Desarrollo de Aplicaciones Web (DAW).

* * *
