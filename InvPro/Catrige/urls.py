from django.urls import path
from Catrige.views import CatrigeModelCreateView, CatrigeModelListView, CatrigeModelDetailView, CatrigeStatusCreateView, \
    CatrigeStatusListView, CatrigeStatusDetailView, CatrigeCreateView, CatrigeListView, CatrigeDetailView

urlpatterns = [
    path('model/create/', CatrigeModelCreateView.as_view()),
    path('model/all/', CatrigeModelListView.as_view()),
    path('model/detail/<int:pk>', CatrigeModelDetailView.as_view()),
    path('status/create/', CatrigeStatusCreateView.as_view()),
    path('status/all/', CatrigeStatusListView.as_view()),
    path('status/detail/<int:pk>', CatrigeStatusDetailView.as_view()),
    path('catrige/create/', CatrigeCreateView.as_view()),
    path('catrige/all/', CatrigeListView.as_view()),
    path('catrige/detail/<int:pk>', CatrigeDetailView.as_view()),



]
