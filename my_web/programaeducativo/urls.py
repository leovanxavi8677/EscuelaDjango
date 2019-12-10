from django.urls import path, include
from .views import RegistrarProgramaEducativo, ObtenerTodosProgramasEducativos, programa_educativo_detalle

urlpatterns = [
    path('RegistrarProgramaEducativo',RegistrarProgramaEducativo,name='RegistrarProgramaEducativo'),
    path('ObtenerTodosProgramasEducativos', ObtenerTodosProgramasEducativos, name='ObtenerTodosProgramasEducativos'),
    path('DetalleProgramaEducativo/<int:programaeducativo_id>/', programa_educativo_detalle,
         name='DetalleProgramaEducativo')
]