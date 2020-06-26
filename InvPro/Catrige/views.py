from django.shortcuts import render
from rest_framework import generics

from Catrige.models import CatrigeModel, JurnalCatrige, Catrige
from Catrige.serializers import CatrigeModelListSerializer, CatrigeStatusSerializer, CatrigeSerializer


class CatrigeModelCreateView(generics.CreateAPIView):
    serializer_class = CatrigeModelListSerializer

class CatrigeModelListView(generics.ListAPIView):
    serializer_class = CatrigeModelListSerializer
    queryset = CatrigeModel.objects.all()

class CatrigeModelDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class =  CatrigeModelListSerializer
    queryset = CatrigeModel.objects.all()


class CatrigeStatusCreateView(generics.CreateAPIView):
    serializer_class = CatrigeStatusSerializer


class CatrigeStatusListView(generics.ListAPIView):
    serializer_class = CatrigeStatusSerializer
    queryset = JurnalCatrige.objects.all()


class CatrigeStatusDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatrigeStatusSerializer
    queryset = JurnalCatrige.objects.all()


class CatrigeCreateView(generics.CreateAPIView):
    serializer_class = CatrigeSerializer


class CatrigeListView(generics.ListAPIView):
    serializer_class = CatrigeSerializer
    queryset = Catrige.objects.all()



class CatrigeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CatrigeSerializer
    queryset = Catrige.objects.all()








