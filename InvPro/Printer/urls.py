from django.urls import path

from Printer.serializers import ZoneDetailView
from Printer.views import *

urlpatterns = [
    path('model/create/', PrinterModelCreateView.as_view()),
    path('model/all/', PrinterModelListView.as_view()),
    path('model/detail/<int:pk>', PrinterModelDetailView.as_view()),
    path('firm/create/', PrinterFirmCreateView.as_view()),
    path('firm/all/', PrinterFirmListView.as_view()),
    path('firm/detail/<int:pk>', PrinterFirmDetailView.as_view()),
    path('zone/create/', ZoneCreateView.as_view()),
    path('zone/all/', ZoneListView.as_view()),
    path('zone/detail/<int:pk>', ZoneDetailView.as_view() )
  ]
