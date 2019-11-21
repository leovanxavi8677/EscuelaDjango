from django.contrib import admin

from .models import Grupo


class GrupoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Grupo, GrupoAdmin)
