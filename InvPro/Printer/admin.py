from django.contrib import admin
from Printer.models import PrinterFirm, PrinterModel, Location,PrinterStatus


class LocationAdmin(admin.ModelAdmin):
    list_display = ('room','titul','floor')

class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ('name','logo')

class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ('name','printerFirm')

class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ('name','image')

admin.site.register(PrinterFirm, PrinterFirmAdmin)
admin.site.register(PrinterModel,PrinterModelAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(PrinterStatus, PrinterStatusAdmin)
