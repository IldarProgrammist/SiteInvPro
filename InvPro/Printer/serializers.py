from rest_framework import serializers
from Printer.models import PrinterModel, PrinterFirm


# Список всех моделей принтеров
class PrinterModelListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterModel
        fields = '__all__'


# Список всех фирм принтеров
class PrinterFirmListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterFirm
        fields = '__all__'

