from django.urls import path

from Printer import views
from Printer.views import PrinterModelDetailView, PrinterModelListView, PrinterModelCreateView, PrinterFirmCreateView, \
    PrinterFirmListView, PrinterFirmDetailView  # PrinterFirmDetailView

urlpatterns = [
    path('model/create/', PrinterModelCreateView.as_view()),
    path('model/all/', PrinterModelListView.as_view()),
    path('model/detail/<int:pk>', PrinterModelDetailView.as_view()),
    path('firm/create/', PrinterFirmCreateView.as_view()),
    path('firm/all/', PrinterFirmListView.as_view()),
    path('firm/detail/<int:pk>', PrinterFirmDetailView.as_view()),
]
