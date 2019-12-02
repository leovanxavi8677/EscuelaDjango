from django.urls import path, include
from .views import RegistrarProgramaEducativo, ObtenerTodosProgramasEducativos

urlpatterns = [
    path('RegistrarProgramaEducativo',RegistrarProgramaEducativo,name='RegistrarProgramaEducativo'),
    path('ObtenerTodosProgramasEducativos', ObtenerTodosProgramasEducativos, name= 'ObtenerTodosProgramasEducativos')
]