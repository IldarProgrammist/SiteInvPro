from rest_framework import generics

from Printer.models import PrinterModel, PrinterFirm
from Printer.serializers import PrinterModelListSerializer, PrinterFirmListSerializer


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
