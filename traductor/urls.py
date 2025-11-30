
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('traducir-contenido/', views.traducitContenido, name='traducir-contenido'),
    path('tts/', views.tts, name='tts'),
]
