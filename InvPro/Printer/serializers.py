from rest_framework import serializers
from Printer.models import *

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

#Место расположение
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrinterStatus
        fields = '__all__'


class PrinterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Printer
        fields = '__all__'
        
    
        
    