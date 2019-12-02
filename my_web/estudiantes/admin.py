from django.contrib import admin

from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    list_display = [
        'get_nombrealumno',
        'get_apellidopaterno',
        'get_apellidomaterno',
        'matricula',
        'semestre',
        'get_programaeducativo',
        'get_materias'
    ]

    search_fields = [
        'nombre',
        'apellidoPaterno',
        'matricula',
        'programaEducativo__nombre'

    ]
    list_display_links = [
        'get_nombrealumno',

    ]

    list_filter = [
        'nombre',
        'semestre'
    ]

    def get_nombrealumno(self, obj):
        return obj.nombre

    def get_apellidopaterno(self, obj):
        return obj.apellidoPaterno

    def get_apellidomaterno(self, obj):
        return obj.apellidoMaterno

    def get_programaeducativo(self, obj):
        return obj.programaEducativo.nombre

    def get_materias(self, obj):
        return "\n".join([m.nombre for m in obj.materias.all()])


admin.site.register(Estudiante, EstudianteAdmin)
