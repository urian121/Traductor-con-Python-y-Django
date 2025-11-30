# Explicación del archivo `vercel.json`

Este archivo configura cómo Vercel debe **construir**, **ejecutar** y **servir** un proyecto Django.

## Estructura completa explicada

```json
{
  "version": 2,
  "builds": [
    {
      "src": "project_core/wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.11" }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config":{ 
        "distDir": "staticfiles"
      }
    }
  ],
  "routes": [
    { 
        "src": "/(.*)", 
        "dest": "project_core/wsgi.py" }
  ]
}
```

## Explicación línea por línea

### `"version": 2`
Indica que se usa la versión 2 del sistema de configuración de Vercel.


## `"builds": [...]`
Define **cómo se deben construir** las partes del proyecto.

### Primer bloque de build → Backend Django

#### `"src": "project_core/wsgi.py"`
Archivo de entrada del backend Django.
Vercel usará este archivo para ejecutar tu aplicación como función serverless.

#### `"use": "@vercel/python"`
Le dice a Vercel que use su runtime de Python.

#### `"config": {...}`
Configuración para la función Python:

* `"maxLambdaSize": "15mb"`
  Aumenta el tamaño máximo permitido para la función Serverless que ejecuta Django.

* `"runtime": "python3.11"`
  Especifica que el proyecto debe ejecutarse con Python 3.11.

### Segundo bloque de build → Archivos estáticos

#### `"src": "build_files.sh"`
Archivo shell que se ejecuta antes del deploy (instala dependencias y colecta estáticos).

#### `"use": "@vercel/static-build"`
Vercel ejecutará el script para generar contenido estático.

#### `"config": { "distDir": "staticfiles" }`

Indica que los archivos estáticos generados estarán en la carpeta `staticfiles`,
la cual Vercel publicará automáticamente.

## `"routes": [...]`
Controla cómo se enrutan las solicitudes del usuario.

### Única regla de rutas

```json
{ 
  "src": "/(.*)", 
  "dest": "project_core/wsgi.py" 
}
```

* `"src": "/(.*)"`
  Captura **todas** las rutas que lleguen al dominio.

* `"dest": "project_core/wsgi.py"`
  Envía todas esas rutas al backend Django.

Esto significa que **Django manejará todas las URL**.


# Conclusión

Este `vercel.json`:

* Ejecuta Django como función serverless con Python 3.11
* Permite una función de hasta 15 MB
* Genera archivos estáticos a través de `build_files.sh`
* Sirve todos los requests desde `wsgi.py`
