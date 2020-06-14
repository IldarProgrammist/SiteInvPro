from rest_framework import generics
from Printer.models import *
from Printer.serializers import PrinterModelListSerializer, PrinterFirmListSerializer, ZoneListSerializer


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


#Зоны на предприятии

class ZoneCreateView(generics.CreateAPIView):
    serializer_class = ZoneListSerializer

class ZoneListView(generics.ListAPIView):
    serializer_class = ZoneListSerializer
    queryset = Zone.objects.all()


class ZoneDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ZoneListSerializer
    queryset = Zone.objects.all()
