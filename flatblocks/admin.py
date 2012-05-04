from django.contrib import admin
from flatblocks.models import FlatBlock


class FlatBlockAdmin(admin.ModelAdmin):
    ordering = ['namespace', ]
    list_display = ('namespace', 'description')
    search_fields = ('namespace', 'description')

admin.site.register(FlatBlock, FlatBlockAdmin)
