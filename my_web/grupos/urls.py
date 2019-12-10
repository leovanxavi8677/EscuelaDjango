from django.urls import path, include
from .views import RegistrarGrupo, ObtenerTodosGrupos, grupo_detalle

urlpatterns = [
    path('RegistrarGrupoNuevo', RegistrarGrupo, name='RegistrarGrupoNuevo'),
    path('ObtenerTodosGrupos', ObtenerTodosGrupos, name='ObtenerTodosGrupos'),
    path('DetalleGrupo/<int:grupo_id>/', grupo_detalle, name='DetalleGrupo')
]
