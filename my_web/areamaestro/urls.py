from django.urls import path, include
from .views import RegistrarAreaMaestro,ObtenerTodosAreasMaestro

urlpatterns = [
    path('RegistrarAreaMaestro',RegistrarAreaMaestro,name='RegistrarAreaMaestro'),
    path('ObtenerTodosAreasMaestro', ObtenerTodosAreasMaestro, name= 'ObtenerTodosAreasMaestro')
]