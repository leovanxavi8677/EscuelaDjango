from django.contrib import admin

from .models import Maestro


class MaestroAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    #se definen los campos que se mostrarán en el listado
    list_display = [
        'get_nombremaestro',
        'cubiculo',
        'numeroTrabajador',
        'estatus',
        'areamaestro'

    ]

    search_fields = [#se definen los campos que definirán para hacer la busqueda
        "numeroTrabajador",'areamaestro__area',
    ]

    list_filter = [
        'areamaestro__area','numeroTrabajador',
    ]

    list_display_links = [
        'get_nombremaestro',

    ]
    #realiz


    #obtiene el nombre del maestro
    def get_nombremaestro(self, obj):
        return obj.nombre + " " + obj.apellidoPaterno + " " + obj.apellidoMaterno
    #ordena
    get_nombremaestro.admin_order_field= 'persona__nombre'




    def get_areamaestro(self, obj):
        return obj.areamaestro.area
    #get_areamaestro.short_description = "Area Maestro"



admin.site.register(Maestro, MaestroAdmin)
