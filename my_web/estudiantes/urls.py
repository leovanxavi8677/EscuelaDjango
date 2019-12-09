from django.urls import path, include
from .views import RegistrarEstudiante, ObtenerTodosEstudiantes, estudainte_detalle

urlpatterns = [
    path('RegistrarEstudianteNuevo', RegistrarEstudiante, name='RegistrarEstudianteNuevo'),
    path('ObtenerTodosEstudiantes', ObtenerTodosEstudiantes, name='ObtenerTodosEstudiantes'),
    path('DetalleEstudiante/<int:estudiante_id>/', estudainte_detalle, name='DetalleEstudiante')
]
