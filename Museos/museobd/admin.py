from django.contrib import admin
from.models import Museo


# Register your models here.
class MuseoAdmin(admin.ModelAdmin):
    readonly_fields = ('updated', 'created')
admin.site.register(Museo,MuseoAdmin)