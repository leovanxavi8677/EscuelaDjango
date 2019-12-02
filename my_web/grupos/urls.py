from django.urls import path, include
from .views import RegistrarGrupo, ObtenerTodosGrupos

urlpatterns = [
    path('RegistrarGrupoNuevo',RegistrarGrupo,name='RegistrarGrupoNuevo'),
    path('ObtenerTodosGrupos', ObtenerTodosGrupos, name= 'ObtenerTodosGrupos')
]