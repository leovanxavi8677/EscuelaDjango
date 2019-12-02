from django.contrib import admin

from .models import Materia


class MateriaAdmin(admin.ModelAdmin):
    list_display = [
        'nombre',
        'estatusMateria',
        'get_areaestudio',
    ]

    search_fields = [
        'nombre',
        'estatusMateria',
        'areaEstudio__area'
    ]

    list_filter = [
        'estatusMateria',
        'areaEstudio__area',
    ]

    list_display_links = [
        'nombre',
        'get_areaestudio',
    ]

    def get_areaestudio(self, obj):
        return obj.areaEstudio.area
admin.site.register(Materia, MateriaAdmin)
