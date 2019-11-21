from django.contrib import admin

from .models import Materia


class MateriaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Materia, MateriaAdmin)
