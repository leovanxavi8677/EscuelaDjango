from django.contrib import admin
from .models import Administrativo


class AdministrativoAdmin(admin.ModelAdmin):
    list_display = [
        'numeroAdministrativo',
        'numeroOficina',
    ]

    search_fields = [
        'numeroAdministrativo',
        'numeroOficina',
    ]

    list_display_links = [
        'numeroAdministrativo',
        'numeroOficina',
    ]

    list_filter = [
        'numeroAdministrativo',
        'numeroOficina',
    ]


admin.site.register(Administrativo, AdministrativoAdmin)
