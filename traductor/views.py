from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from deep_translator import GoogleTranslator
import json
from . models import *  # Importando todos mis modelos (idiomas)
from gtts import gTTS
from io import BytesIO


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


def tts(request):
    try:
        if request.method != 'POST':
            return JsonResponse({'error': 'Método no permitido'}, status=405)

        data = json.loads(request.body)
        texto = data.get('texto')
        lenguaje_destino = data.get('lenguajeDestino')
        if not texto or not lenguaje_destino:
            return JsonResponse({'error': 'Faltan parámetros'}, status=400)

        tts = gTTS(text=texto, lang=lenguaje_destino)
        buf = BytesIO()
        tts.write_to_fp(buf)
        buf.seek(0)

        response = HttpResponse(buf.read(), content_type='audio/mpeg')
        response['Content-Disposition'] = 'inline; filename="tts.mp3"'
        return response
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
