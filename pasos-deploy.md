# 🚀 Deploy de una aplicación **Django** en **Vercel**

## 1. Requisitos previos
* Proyecto funcionando en GitHub.
* Cuenta en Vercel.


## 2. Preparar el proyecto Django

###  Exponer variable `app` en WSGI

Archivo: `your_project/wsgi.py`

```python
application = get_wsgi_application()
app = application  # Vercel busca esta variable
```

### Permitir hosts de Vercel

Archivo: `your_project/settings.py`

```python
ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']
```

### Desactivar modo debug en `your_project/settings.py`

```python
DEBUG = False
```

### Configurar `STATIC_ROOT` en `settings.py`
Será la carpeta donde Vercel guardará los archivos estáticos después del collectstatic.
Esta debe coincidir con el nombre de la carpeta en `"distDir": "staticfiles"`


```python
STATIC_URL = 'static/'

# Directorio donde se guardarán los archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# ⭐ IMPORTANTE PARA PRODUCCIÓN (VERCEL)
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
```

### Servir archivos estáticos con Whitenoise

```python
MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # ...
]
```

## 3. Dependencias del proyecto
Generar `requirements.txt`:

```bash
pip freeze > requirements.txt
```

## 4. Script para archivos estáticos

Crear `build_files.sh` en la raíz:

```bash
# build_files.sh
pip install -r requirements.txt
python3.11 manage.py collectstatic --no-input --clear
```

## 5. Configurar **vercel.json**
Crear en la raíz del proyecto:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "your_project/wsgi.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "15mb",
        "runtime": "python3.11"
      }
    },
    {
      "src": "build_files.sh",
      "use": "@vercel/static-build",
      "config": { 
        "distDir": "staticfiles"
      }
    }
  ],
  "routes": [
    { 
      "src": "/(.*)", 
      "dest": "your_project/wsgi.py" 
    }
  ]
}
```

## 6. Deploy

1. Subir todo a GitHub.
2. Importar el repositorio en Vercel.
3. Deploy automático.

