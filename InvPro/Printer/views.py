from rest_framework import generics
from Printer.models import PrinterModel, PrinterFirm
from Printer.serializers import *

class PrinterModelCreateView(generics.CreateAPIView):
    serializer_class = PrinterModelListSerializer


class PrinterModelListView(generics.ListAPIView):
    serializer_class = PrinterModelListSerializer
    queryset = PrinterModel.objects.all()


class PrinterModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrinterModelListSerializer
    queryset = PrinterModel.objects.all()


# Информация о фирмах принтеров

class PrinterFirmCreateView(generics.CreateAPIView):
    serializer_class = PrinterFirmListSerializer


class PrinterFirmListView(generics.ListAPIView):
    serializer_class = PrinterFirmListSerializer
    queryset = PrinterFirm.objects.all()


class PrinterFirmDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PrinterFirmListSerializer
    queryset = PrinterFirm.objects.all()

class LocationCreateView(generics.CreateAPIView):
    serializer_class = LocationSerializer


class LocationListView(generics.ListAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

class LocationDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LocationSerializer
    queryset = Location.objects.all()

#Статус

class StatusCreateView(generics.CreateAPIView):
    serializer_class = StatusSerializer


class StatusListView(generics.ListAPIView):
    serializer_class = StatusSerializer
    queryset = PrinterStatus.objects.all()

class StatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StatusSerializer
    queryset = PrinterStatus.objects.all()

    