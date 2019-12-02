from django.contrib import admin

from .models import AreaMaestro


class AreaMaestroAdmin(admin.ModelAdmin):
    list_display = [
        'area'
    ]

    search_fields = [
        'area'
    ]
    list_filter = [
        'area'
    ]

    list_display_links = [
        'area'
    ]




admin.site.register(AreaMaestro, AreaMaestroAdmin)

