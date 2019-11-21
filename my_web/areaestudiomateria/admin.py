from django.contrib import admin

from .models import AreaEstudioMateria


class AreaEstudioMateriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(AreaEstudioMateria, AreaEstudioMateriaAdmin)
