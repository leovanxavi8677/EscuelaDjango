from django.contrib import admin

from .models import ProgramaEducativo


class ProgramaEducativoAdmin(admin.ModelAdmin):
    pass


admin.site.register(ProgramaEducativo, ProgramaEducativoAdmin)
