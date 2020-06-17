from django.contrib import admin
from Printer.models import *

#
class LocationAdmin(admin.ModelAdmin):
    list_display = ('room', 'titul', 'floor')



class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')


class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'printerFirm')


class PrinterStatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')



class PrinterAdmin(admin.ModelAdmin):
    list_display = ('serialNamber', 'ip')


class StatusPAdmin(admin.ModelAdmin):
    list_display = ('printer', 'status', 'dateChange', 'discription')

class LocAdmin(admin.ModelAdmin):
    list_display = ('serialNamber','numberRoom','typeRoom','numberTutul','floor','zone', 'dateChange')


admin.site.register(PrinterFirm, PrinterFirmAdmin)
admin.site.register(PrinterModel, PrinterModelAdmin)
admin.site.register(LocationPrinter, LocAdmin)
admin.site.register(Zone)
admin.site.register(TypeRoom)
admin.site.register(Printer, PrinterAdmin)
admin.site.register(StatusP, StatusPAdmin)
admin.site.register(Status)
