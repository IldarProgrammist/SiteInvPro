from django.contrib import admin
from Catrige.models import Color, CatrigeModel, StatusCatrige, Catrige, JurnalCatrige


class CatrigeModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'printerModel')
    search_fields = ['color__name']



class CatrigeAdmin(admin.ModelAdmin):
    list_display = ('serialNumber', 'modelCatrige','original')
    search_fields = ['serialNumber']


class StatusCAdmin(admin.ModelAdmin):
    list_display = ('serialNumber','catrigeStatus','dateChange')
    search_fields = ['serialNumber__serialNumber']

class  ExtraditionAdmin(admin.ModelAdmin):
    list_display = ('serialNumberCatrige','statusExtradition','dataExtradition')

class  JurnalCatrigeAdmin(admin.ModelAdmin):
    list_display = ('serialNumberCatrige','status','dateExtation')
    search_fields = ['serialNumberCatrige__serialNumber']



admin.site.register(Color)
admin.site.register(CatrigeModel, CatrigeModelAdmin)
admin.site.register(StatusCatrige)
admin.site.register(Catrige, CatrigeAdmin)
admin.site.register(JurnalCatrige, JurnalCatrigeAdmin)
