from django.contrib import admin
from Catrige.models import Color, CatrigeModel, StatusCatrige


class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ['color__name']


admin.site.register(Color)
admin.site.register(CatrigeModel, CatrigeModelAdmin)
admin.site.register(StatusCatrige)