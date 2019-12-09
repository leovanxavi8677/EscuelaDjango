from django.urls import path, include
from .views import RegistrarAreaMaestro, ObtenerTodosAreasMaestro, area_maestro_detalle

urlpatterns = [
    path('RegistrarAreaMaestro/', RegistrarAreaMaestro, name='RegistrarAreaMaestro'),
    path('ObtenerTodosAreasMaestro/', ObtenerTodosAreasMaestro, name='ObtenerTodosAreasMaestro'),
    path('DetalleAreaMaestro/<int:area_id>/', area_maestro_detalle, name='DetalleAreaMaestro')
]