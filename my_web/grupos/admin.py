from django.contrib import admin

from .models import Grupo


class GrupoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'numeroAlumnos',
        'estatus',
        'get_materia',
        'get_maestro'
    ]

    search_fields = [
        'nombre',
        'estatus',
        'maestroAsignado__nombre'
    ]

    list_filter = [
        'nombre',
        'maestroAsignado__nombre',
        'estatus',
    ]

    def get_materia(self, obj):
        return obj.materia.nombre

    def get_maestro(self, obj):
        return obj.maestroAsignado.nombre

admin.site.register(Grupo, GrupoAdmin)
