from django.contrib import admin
from Printer.models import *


class LocationAdmin(admin.ModelAdmin):
    list_display = ('room', 'titul', 'floor')


class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'printerFirm')


class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')


class LocationPrinterAdmin(admin.ModelAdmin):
    list_display = ('numberRoom', 'typeRoom', 'numberTutul', 'floor', 'zone')


admin.site.register(PrinterFirm, PrinterFirmAdmin)
admin.site.register(PrinterModel, PrinterModelAdmin)
admin.site.register(Zone)
admin.site.register(TypeRoom)
admin.site.register(LocationPrinter, LocationPrinterAdmin)
