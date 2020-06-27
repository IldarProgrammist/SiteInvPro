from django.contrib import admin
from Printer.models import *


@admin.register(PrinterFirm)
class PrinterFirmAdmin(admin.ModelAdmin):
    list_display = ('name', 'logo')#


@admin.register(PrinterModel)
class PrinterModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'printerFirm')


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    list_display = ('serialNamber', 'modelPrinter','ip')

@admin.register(StatusP)
class StatusPAdmin(admin.ModelAdmin):
    list_display = ('printer', 'status', 'dateChangeStatus', 'discription')
    search_fields = ['status__name']


@admin.register(LocationPrinter)
class LocAdmin(admin.ModelAdmin):
    list_display = ('serialNamber','numberRoom','typeRoom','numberTutul','floor','zone', 'dateChange')
    search_fields = ['serialNamber__serialNamber']


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(TypeRoom)
class TypeRoomAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    list_display = ['name']



