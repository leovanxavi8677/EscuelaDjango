from django.urls import path, include
from .views import RegistrarMaestro, ObtenerTodosMaestros, maestro_detalle
urlpatterns = [
    path('RegistrarMaestro/', RegistrarMaestro, name='RegistrarMaestro'),
    path('ObtenerTodosMaestros/', ObtenerTodosMaestros, name='ObtenerTodosMaestros'),
    path('DetalleMaestro/<int:maestro_id>/', maestro_detalle, name='DetalleMaestro')
]
