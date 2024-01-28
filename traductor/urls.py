
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('traducir-contenido/', views.traducitContenido, name='traducir-contenido'),
]
