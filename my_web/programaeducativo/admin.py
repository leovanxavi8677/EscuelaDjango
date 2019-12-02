from django.contrib import admin

from .models import ProgramaEducativo


class ProgramaEducativoAdmin(admin.ModelAdmin):
    list_display = [
        'nombre'
    ]

    search_fields = [
        'nombre'
    ]

    list_filter = [
        'nombre'
    ]
    list_display_links = [
        'nombre'
    ]


admin.site.register(ProgramaEducativo, ProgramaEducativoAdmin)
