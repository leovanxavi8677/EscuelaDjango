from django.contrib import admin

from .models import Estudiante

class EstudianteAdmin(admin.ModelAdmin):
    pass


admin.site.register(Estudiante, EstudianteAdmin)
