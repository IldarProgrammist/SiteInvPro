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


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPrinter
        fields = '__all__'


class LocationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = LocationPrinter
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'


class StatusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'

class StatusPSerializer(serializers.ModelSerializer):
    class Meta:
        model = StatusP
        fields = '__all__'