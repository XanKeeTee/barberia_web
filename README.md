<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>BarberGestion - README</title>
    <style>
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.6;
            color: #24292f;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
            background-color: #ffffff;
        }
        h1, h2, h3 {
            margin-top: 24px;
            margin-bottom: 16px;
            font-weight: 600;
            line-height: 1.25;
        }
        h1 {
            font-size: 2em;
            padding-bottom: 0.3em;
            border-bottom: 1px solid #d0d7de;
        }
        h2 {
            font-size: 1.5em;
            padding-bottom: 0.3em;
            border-bottom: 1px solid #d0d7de;
        }
        h3 {
            font-size: 1.25em;
        }
        p, ul, pre {
            margin-top: 0;
            margin-bottom: 16px;
        }
        ul {
            padding-left: 2em;
        }
        li {
            margin-top: 0.25em;
        }
        pre {
            background-color: #f6f8fa;
            border-radius: 6px;
            padding: 16px;
            overflow: auto;
            font-size: 85%;
            line-height: 1.45;
        }
        code {
            font-family: ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, Liberation Mono, monospace;
            background-color: rgba(175, 184, 193, 0.2);
            padding: 0.2em 0.4em;
            border-radius: 6px;
            font-size: 85%;
        }
        pre code {
            background-color: transparent;
            padding: 0;
            font-size: 100%;
        }
        .badges {
            margin-bottom: 16px;
        }
        .badges img {
            margin-right: 5px;
            margin-bottom: 5px;
        }
        .task-list-item {
            list-style-type: none;
        }
        .task-list-item input {
            margin: 0 0.2em 0.25em -1.6em;
            vertical-align: middle;
        }
        hr {
            height: 0.25em;
            padding: 0;
            margin: 24px 0;
            background-color: #d0d7de;
            border: 0;
        }
    </style>
</head>
<body>

    <h1>💈 BarberGestion - Sistema de Reservas para Barberías</h1>

    <div class="badges">
        <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
        <img src="https://img.shields.io/badge/Bootstrap_5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white" alt="Bootstrap">
        <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript">
    </div>

    <p>BarberGestion es una aplicación web integral desarrollada para la digitalización y automatización de citas en barberías y peluquerías. Diseñada para mejorar la experiencia del cliente y optimizar el tiempo de los profesionales, eliminando la gestión telefónica tradicional.</p>

    <h2>🚀 Características Principales</h2>

    <h3>Para el Cliente</h3>
    <ul>
        <li><strong>Reserva de Citas Inteligente:</strong> Sistema de reservas paso a paso (Servicio > Profesional > Fecha > Hora).</li>
        <li><strong>Catálogo Visual:</strong> Galería de servicios y estilos integrados en la plataforma.</li>
        <li><strong>Horarios Dinámicos:</strong> El sistema diferencia automáticamente los horarios entre semana y los fines de semana (ej. Sábados solo mañanas), adaptando la disponibilidad en tiempo real.</li>
        <li><strong>Control de Disponibilidad:</strong> Bloqueo automático de horas ya reservadas o pasadas en el día actual.</li>
    </ul>

    <h3>Para la Administración (Barberos/Gerencia)</h3>
    <ul>
        <li><strong>Panel de Control:</strong> Gestión completa a través del panel de administración de Django.</li>
        <li><strong>Gestión de Personal:</strong> Creación y edición de perfiles de barberos.</li>
        <li><strong>Gestión de Servicios:</strong> Control de precios, duración y catálogo de cortes.</li>
        <li><strong>Control de Agenda:</strong> Visualización en tiempo real de las citas diarias.</li>
    </ul>

    <h2>🛠️ Stack Tecnológico</h2>
    <ul>
        <li><strong>Backend:</strong> Python 3.11+ / Django 5.x</li>
        <li><strong>Frontend:</strong> HTML5, CSS3, JavaScript Vanilla</li>
        <li><strong>Framework UI:</strong> Bootstrap 5</li>
        <li><strong>Librerías Adicionales:</strong> Flatpickr (Calendario interactivo)</li>
        <li><strong>Base de Datos:</strong> SQLite (Desarrollo) / PostgreSQL (Preparado para Producción)</li>
    </ul>

    <h2>⚙️ Instalación y Despliegue Local</h2>
    <p>Sigue estos pasos para ejecutar el proyecto en tu entorno local.</p>

    <h3>1. Clonar el repositorio</h3>
<pre><code>git clone https://github.com/tu-usuario/barber-gestion.git
cd barber-gestion</code></pre>

    <h3>2. Crear y activar el entorno virtual</h3>
    <p>En Windows:</p>
<pre><code>python -m venv env
.\env\Scripts\activate</code></pre>
    <p>En macOS / Linux:</p>
<pre><code>python3 -m venv env
source env/bin/activate</code></pre>

    <h3>3. Instalar dependencias</h3>
<pre><code>pip install -r requirements.txt</code></pre>

    <h3>4. Configurar la Base de Datos (Migraciones)</h3>
<pre><code>python manage.py makemigrations
python manage.py migrate</code></pre>

    <h3>5. Crear el superusuario (Administrador)</h3>
<pre><code>python manage.py createsuperuser</code></pre>
    <p><em>(Sigue las instrucciones en pantalla para configurar email y contraseña).</em></p>

    <h3>6. Ejecutar el servidor de desarrollo</h3>
<pre><code>python manage.py runserver</code></pre>

    <p>La aplicación estará disponible en: <code>http://127.0.0.1:8000/</code><br>
    El panel de administración en: <code>http://127.0.0.1:8000/admin/</code></p>

    <h2>📂 Estructura del Proyecto</h2>
  <pre><code>barber_gestion/
  ├── manage.py
  ├── core/                   # Configuración principal de Django
  ├── gestion_citas/          # Aplicación principal
  │   ├── models.py           # Modelos de base de datos (Barbero, Servicio, Cita)
  │   ├── views.py            # Lógica de negocio y controladores
  │   ├── urls.py             # Rutas de la aplicación
  │   ├── templates/          # Plantillas HTML (incluye lógica JS dinámica)
  │   └── static/             # Archivos CSS, JS e imágenes estáticas
  └── db.sqlite3              # Base de datos local</code></pre>

    <h2>📝 Próximas Implementaciones (Roadmap)</h2>
    <ul>
        <li class="task-list-item"><input type="checkbox" disabled> Integración de pasarela de pago (Stripe/PayPal) para reservas con fianza.</li>
        <li class="task-list-item"><input type="checkbox" disabled> Envío automático de recordatorios por WhatsApp o Correo Electrónico.</li>
        <li class="task-list-item"><input type="checkbox" disabled> Panel estadístico (Dashboard) de ingresos y citas mensuales para el administrador.</li>
    </ul>

    <h2>📄 Licencia</h2>
    <p>Este proyecto es parte de un entorno educativo para el ciclo de Desarrollo de Aplicaciones Web (DAW).</p>

    <hr>
    <p><em>Desarrollado con ❤️ para el proyecto final de DAW.</em></p>

</body>
</html>
