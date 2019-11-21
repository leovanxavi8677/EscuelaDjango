from django.contrib import admin

from .models import Maestro


class MaestroAdmin(admin.ModelAdmin):
    pass


admin.site.register(Maestro, MaestroAdmin)
