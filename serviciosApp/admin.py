from django.contrib import admin
from serviciosApp.models import misServicios

# Register your models here.
class misserviciosAdmin(admin.ModelAdmin):
    readonly_fields = ('create','update')

admin.site.register(misServicios,misserviciosAdmin)