from django.shortcuts import render, HttpResponse


def inicio(request):
    return render(request, 'inicio.html')


def traducitContenido(request):
    return HttpResponse("Hola Mundo")
