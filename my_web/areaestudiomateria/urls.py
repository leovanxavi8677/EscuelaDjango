from django.urls import path, include
from .views import RegistrarAreaEstudioMateria, ObtenerTodosAreasEstudioMateria

urlpatterns = [
    path('RegistrarAreaEstudioMateria', RegistrarAreaEstudioMateria, name='RegistrarAreaEstudioMateria'),
    path('ObtenerTodosAreasEstudioMateria', ObtenerTodosAreasEstudioMateria, name='ListingAreasEstudioMaterias')
]