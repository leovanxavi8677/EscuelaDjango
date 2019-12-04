from django.urls import path, include
from .views import iniciar_sesion,mostrar_pagina_principal
urlpatterns = [
    path('iniciosesion/', iniciar_sesion, name='iniciosesion'),
    path('pagina_principal', mostrar_pagina_principal, name='paginaprincipal')
]