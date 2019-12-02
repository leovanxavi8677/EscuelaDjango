from django.urls import path, include
from .views import RegistrarMateria, ObtenerTodasMaterias

urlpatterns = [
    path('RegistrarMateria', RegistrarMateria, name='RegistrarMateria'),
    path('ObtenerTodasMaterias', ObtenerTodasMaterias, name= 'ObtenerTodasMaterias')
]