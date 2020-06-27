from django.contrib import admin
from Catrige.models import  CatrigeModel, Catrige, JurnalCatrige


@admin.register(CatrigeModel)
class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'color', 'printerModel']
    search_fields = ['name']


@admin.register(Catrige)
class CatrigeAdmin(admin.ModelAdmin):
    list_display = ['serialNumber', 'modelCatrige', 'original']
    search_fields = ['serialNumber']
    autocomplete_fields = ('modelCatrige',)


@admin.register(JurnalCatrige)
class JurnalCatrigeAdmin(admin.ModelAdmin):
    list_display = ('serialNumberCatrige','status','dateExtation')
    search_fields = ['serialNumberCatrige__serialNumber']
