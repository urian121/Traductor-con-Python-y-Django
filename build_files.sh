# build_files.sh para generar archivos estáticos

# Instalar dependencias
pip install -r requirements.txt

# # Generar archivos estáticos de forma limpia y sin intervención
python3 manage.py collectstatic --no-input --clear

# --no-input → evita cualquier pregunta de confirmación (ideal para deploy).
# --clear → borra los archivos estáticos previos antes de copiar los nuevos.