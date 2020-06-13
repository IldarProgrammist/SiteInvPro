from django.contrib import admin
from Printer.models import *

class LocationAdmin(admin.ModelAdmin):
    list_display = ('room','titul','floor')

class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ('name','logo')

class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ('name','printerFirm')

class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ('name','image')

class PrinterAdmin(admin.ModelAdmin):
    list_display = ('serialNumber', 'ipAdress', 'printerModel','location','printerStatus')

admin.site.register(PrinterFirm, PrinterFirmAdmin)
admin.site.register(PrinterModel,PrinterModelAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PrinterStatus, PrinterStatusAdmin)
admin.site.register(Printer, PrinterAdmin)