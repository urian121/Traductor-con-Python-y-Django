### Creando un Traductor con Python y Django

##### El proyecto "Traductor Multilingüe" busca crear una aplicación web que permita a los usuarios traducir texto entre varios idiomas de manera rápida y sencilla. Utilizando el poder de Python y el marco de desarrollo web Django, este proyecto ofrece una solución eficiente y accesible para las necesidades de traducción de los usuarios.

1.  Crear un entorno virtual, hay muchas formas

        Opción 1: Crear entorno virtual con el paquete virtualenv
        Si no tienes instalado virtualenv puedes instalarlo de forma global en el sistema atraves de https://pypi.org/project/virtualenv/
        pip install virtualenv ->Instalar de forma global
        virtualenv env ->Crear entorno
        virtualenv --version ->Ver la versión de virtualenv

        Opción 2: Crear un entorno virtual con el paquete que ya viene por defecto en las ultimas versiones de Python
        python -m venv env

2.  Activar entorno virtual

        . env/Script/activate ->para Windows
        . env/bin/activate -> Para Mac
        deactivate -->Para desactivar mi entorno virtual

3.  Instalar django desde el manejador de paquete de Python Pip, ya dentro del entorno virtual.

        pip install Django
        Nota: para instalar Django en una version especifica
        pip install Django==4.2.4

4.  Instalar el paquete (deep_translator) el cual nos ayudará a traducir el contenido

        pip install deep_translator

5.  Instalar Driver para conectar Gestor de BD MySQL con Django, con el fin de crear una tabla para almacenar los idiomas disponibles

        pip install mysqlclient

6.  Crear el proyecto con django

        `django-admin startproject project_core .`
        El punto . es crucial le dice al script que instale Django en el directorio actual

        Ya en este punto se puede correr el proyecto que a creado Django,
        python manage.py runserver

7.  Crear mi primera aplicación en Django

        python manage.py startapp traductor

8.  Instalar nuestra aplicación (traductor) ya creada en el proyecto, en el archivo settings.py

        archivo settings.py
        INSTALLED_APPS = [
        ----,
        'traductor',
        ]

9.  Crear las migraciones y correrlas

        python manage.py makemigrations -> Creando migraciones
        python manage.py migrate         -> Correr migraciones

10. Correr el proyecto

        python manage.py runserver
        Revisar la consola y visitar la URL http://127.0.0.1:8000

11. Crear el archivo urls.py en la aplicación (traductor)

        from django.urls import path
        from . import views

                urlpatterns = [
                        path('', views.inicio, name='inicio'),
                        path('registrar_empleado/', views.registrar_empleado,
                                name='registrar_empleado'),
                        path('empleados/', views.listar_empleados, name='listar_empleados'),
                ]

12. Conectar las URLS de mi aplicación con el projecto, para esto vamos al archivo uls.py del projecto
    from django.urls import path, include

        urlpatterns = [
                path('admin/', admin.site.urls),
                path("", include('empleados.urls'))
        ]

13. Crear la carpeta 'templates' dentro de la aplicación donde estarán mis archivos.html

14. Crear la carpeta 'static' dentro de mi aplicacion, aqui estaran archivos
    estaticos (css, js, imagenes, etc..)

15. Correr archivo requirement.txt para instalar todas las dependencias del proyecto

        pip install -r requirements.txt

16. Información de Paquete
    https://pypi.org/project/deep-translator/

###### El paquete deep-translator de Python. Este paquete proporciona una interfaz para traducir texto utilizando varios servicios de traducción en línea, como Google Translate, Microsoft Translator, y otros.

#### Resultado final

![](https://raw.githubusercontent.com/urian121/imagenes-proyectos-github/master/traductor-con-python.png)

### Expresiones de Gratitud 🎁

    Comenta a otros sobre este proyecto 📢
    Invita una cerveza 🍺 o un café ☕
    Paypal iamdeveloper86@gmail.com
    Da las gracias públicamente 🤓.

## No olvides SUSCRIBIRTE 👍
