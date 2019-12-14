from django.urls import path
from .views import RegistrarAdministrativo, ObtenerTodosAdministrativos, administrativo_detalle

urlpatterns = [
    path('RegistrarAdministrativoNuevo', RegistrarAdministrativo, name='RegistrarAdministrativoNuevo'),
    path('ObtenerTodosAdministrativos', ObtenerTodosAdministrativos, name='ObtenerTodosAdministrativos'),
    path('DetalleAdministrativo/<int:administrativo_id>/', administrativo_detalle, name='DetalleAdministrativo'),
]