from django.contrib import admin

from .models import Persona


class PersonaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'apellidoPaterno',
        'apellidoMaterno',
        'fechaNacimiento',
        'edad',
        'nivelEstudios',
        'genero',
        'nivelAcceso',
    ]
    search_fields = [
        'nombre',
        'nivelEstudios',
        'genero',
        'nivelAcceso'
    ]

    list_filter = [
        'nivelEstudios',
        'genero',
        'nivelAcceso'
    ]

    list_display_links = [
        'nombre'
    ]

admin.site.register(Persona, PersonaAdmin)
