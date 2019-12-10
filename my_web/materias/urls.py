from django.urls import path, include
from .views import RegistrarMateria, ObtenerTodasMaterias, materia_detalle

urlpatterns = [
    path('RegistrarMateria', RegistrarMateria, name='RegistrarMateria'),
    path('ObtenerTodasMaterias', ObtenerTodasMaterias, name='ObtenerTodasMaterias'),
    path('DetalleMateria/<int:materia_id>/', materia_detalle, name='DetalleMateria')
]