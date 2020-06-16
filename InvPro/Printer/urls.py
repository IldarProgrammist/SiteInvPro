from django.urls import path
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
    path('zone/detail/<int:pk>', ZoneDetailView.as_view()),
    path('typeroom/create/', TypeRoomCreateView.as_view()),
    path('typeroom/all/',    TypeRoomListView.as_view()),
    path('typeroom/detail/<int:pk>', TypeRoomDetailView.as_view()),
    path('location/create/', LocationCreatetView.as_view()),
    path('location/all/',    LocationListView.as_view()),
    path('location/detail/<int:pk>', LocationDetailView.as_view()),
    path('status/create/', StatusCreateView.as_view()),
    path('status/all/', StatusListView.as_view()),
    path('status/detail/<int:pk>', StatusDetailView.as_view()),
    path('statusp/create/',  PrinterStatusCreateView.as_view()),
    path('statusp/all/', StatusPListView.as_view()),
    path('statusp/detail/<int:pk>',StatusPDetailView.as_view())
]
