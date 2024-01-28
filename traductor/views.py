from django.shortcuts import render
from django.http import JsonResponse
from deep_translator import GoogleTranslator
import json
from . models import *  # Importando todos mis modelos (idiomas)


def inicio(request):
    return render(request, 'inicio.html', {"idiomas": listaIdiomas(request)})


def traducitContenido(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            texto_a_traducir = data.get('texto')
            lenguaje_origen = data.get('lenguajeOrigen')
            lenguaje_destino = data.get('lenguajeDestino')
            # print(lenguaje_destino, lenguaje_origen)

            # source=representa el lenguajes de origen, target= representa el lenguaje de destino
            traduccion = GoogleTranslator(
                source=lenguaje_origen, target=lenguaje_destino).translate(texto_a_traducir)

            return JsonResponse({'status': 200, 'data': traduccion})
        else:
            return JsonResponse({'error': 'Método no permitido'}, status=405)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


# Función que retorna una lista de todos los idiomas disponibles para traducir
def listaIdiomas(resquest):
    return Idioma.objects.all().order_by('idioma')
