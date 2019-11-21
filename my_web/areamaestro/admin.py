from django.contrib import admin

from .models import AreaMaestro


class AreaMaestroAdmin(admin.ModelAdmin):
    pass


admin.site.register(AreaMaestro, AreaMaestroAdmin)

