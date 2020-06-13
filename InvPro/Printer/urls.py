from django.urls import path
from Printer import views
from Printer.views import *

urlpatterns = [
    path('model/create/', PrinterModelCreateView.as_view()),
    path('model/all/', PrinterModelListView.as_view()),
    path('model/detail/<int:pk>', PrinterModelDetailView.as_view()),
    path('firm/create/', PrinterFirmCreateView.as_view()),
    path('firm/all/', PrinterFirmListView.as_view()),
    path('firm/detail/<int:pk>', PrinterFirmDetailView.as_view()),
    path('location/create/', LocationCreateView.as_view()),
    path('location/all/', LocationListView.as_view()),
    path('location/detail/<int:pk>', LocationDetailView.as_view()),
    path('status/create/', StatusCreateView.as_view()),
    path('status/all/', StatusListView.as_view()),
    path('starus/detail/<int:pk>', StatusDetailView.as_view()),
    path('printer/create/', PrinterCreateView.as_view()),
    path('printer/all/', PrinterListView.as_view()),
    path('printer/detail/<int:pk>', PrinterDetailView.as_view()),
]
