from django.urls import path, include
from .views import RegistrarAreaEstudioMateria, ObtenerTodosAreasEstudioMateria

urlpatterns = [
    path('RegistrarAreaEstudioMateria', RegistrarAreaEstudioMateria, name='RegistrarNuevaAreaEstudioMateria'),
    path('ObtenerTodosAreasEstudioMateria', ObtenerTodosAreasEstudioMateria, name='ListingAreasEstudioMaterias')
]