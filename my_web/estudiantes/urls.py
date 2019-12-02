from django.urls import path, include
from .views import RegistrarEstudiante, ObtenerTodosEstudiantes

urlpatterns = [
    path('RegistrarEstudianteNuevo', RegistrarEstudiante, name='RegistrarEstudianteNuevo'),
    path('ObtenerTodosEstudiantes', ObtenerTodosEstudiantes, name='ObtenerTodosEstudiantes')
]
