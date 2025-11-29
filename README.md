# Creando un Traductor con Python y Django

El proyecto "Traductor Multilingüe" busca crear una aplicación web que permita a los usuarios traducir texto entre varios idiomas de manera rápida y sencilla. Utilizando el poder de Python y el marco de desarrollo web Django, este proyecto ofrece una solución eficiente y accesible para las necesidades de traducción de los usuarios.

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/traductor-con-python.png)

## Pasos de Instalación

### 1. Crear un entorno virtual

**Opción 1: virtualenv**

```bash
pip install virtualenv
virtualenv env
virtualenv --version
```

**Opción 2: módulo integrado de Python**

```bash
python -m venv env
```

### 2. Activar entorno virtual

```bash
# Windows
env\Scripts\activate

# Mac / Linux
source env/bin/activate

# Desactivar
deactivate
```

### 3. Instalar Django

```bash
pip install Django
# Versión específica
pip install Django==4.2.4
```

### 4. Instalar paquete de traducción

```bash
pip install deep_translator
```

### 5. Instalar driver de MySQL

```bash
pip install mysqlclient
```

### 6. Crear el proyecto

```bash
django-admin startproject project_core .
python manage.py runserver
```

### 7. Crear la aplicación principal

```bash
python manage.py startapp traductor
```

### 8. Registrar la app en `settings.py`

```python
INSTALLED_APPS = [
    ...,
    'traductor',
]
```

### 9. Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### 10. Ejecutar el proyecto

```bash
python manage.py runserver
```

Visita: [http://127.0.0.1:8000](http://127.0.0.1:8000)

### 11. Crear `urls.py` dentro de la app

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]
```

### 12. Conectar URLs de la app al proyecto

En `urls.py` del proyecto:

```python
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('traductor.urls')),
]
```

### 13. Crear carpeta `templates` dentro de la app

Para tus archivos `.html`.

### 14. Crear carpeta `static` dentro de la app

Para CSS, JS e imágenes.

### 15. Instalar dependencias desde requirements

```bash
pip install -r requirements.txt
```

### 16. Información del paquete

[https://pypi.org/project/deep-translator/](https://pypi.org/project/deep-translator/)
El paquete deep-translator permite traducir texto usando varios servicios como Google Translate y Microsoft Translator.

## Expresiones de Gratitud 🎁

* Recomienda este proyecto 📢
* Invita una cerveza 🍺 o un café ☕
* PayPal: **[iamdeveloper86@gmail.com](mailto:iamdeveloper86@gmail.com)**
* Agradece públicamente 🤓
* ¡No olvides SUSCRIBIRTE! 👍
