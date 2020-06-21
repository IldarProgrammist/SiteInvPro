from django.contrib import admin
from Catrige.models import Color, CatrigeModel, StatusCatrige, Catrige, StarusC


class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')
    search_fields = ['color__name']

class CatrigeAdmin(admin.ModelAdmin):
    list_display = ('serialNumber', 'modelCatrige')
    search_fields = ['modelCatrige__name']

class StatusCAdmin(admin.ModelAdmin):
    list_display = ('serialNumber','catrigeStatus','dateChange')
    search_fields = ['serialNumber__serialNumber']


admin.site.register(Color)
admin.site.register(CatrigeModel, CatrigeModelAdmin)
admin.site.register(StatusCatrige)
admin.site.register(Catrige, CatrigeAdmin)
admin.site.register(StarusC, StatusCAdmin)