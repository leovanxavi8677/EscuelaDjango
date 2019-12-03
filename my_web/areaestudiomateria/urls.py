from django.urls import path, include
from .views import RegistrarAreaEstudioMateria, ObtenerTodosAreasEstudioMateria, area_estudio__materia_detalle
urlpatterns = [
    path('RegistrarAreaEstudioMateria/', RegistrarAreaEstudioMateria, name='RegistrarNuevaAreaEstudioMateria'),
    path('ObtenerTodosAreasEstudioMateria/', ObtenerTodosAreasEstudioMateria, name='ListingAreasEstudioMaterias'),
    path('DetalleAreaMateria/<int:area_id>/', area_estudio__materia_detalle, name='DetalleAreaEstudio')
]