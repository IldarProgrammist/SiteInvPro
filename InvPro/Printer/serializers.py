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


class ZoneListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'


class ZoneDetailView(serializers.ModelSerializer):
    class Meta:
        model = Zone
        fields = '__all__'

        

class TypeRoomListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = '__all__'


class TypeRoomDetailView(serializers.ModelSerializer):
    class Meta:
        model = TypeRoom
        fields = '__all__'

