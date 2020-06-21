from django.contrib import admin
from Catrige.models import Color, CatrigeModel


class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ['color__name']


admin.site.register(Color)
admin.site.register(CatrigeModel, CatrigeModelAdmin)
