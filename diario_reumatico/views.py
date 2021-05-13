from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import  DorSerializer, HumorSerializer, RemediosSerializer, RigidezSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dor, Humor, Remedios, Rigidez
from rest_framework.permissions import IsAuthenticated

class DorView(ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    serializer_class = DorSerializer
    def get_queryset(self):
        queryset = Dor.objects.all()
        user = self.request.user
        return queryset.filter(email=user)

class HumorView(ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    serializer_class = HumorSerializer
    def get_queryset(self):
        queryset = Humor.objects.all()
        user = self.request.user
        return queryset.filter(email=user)

class RemediosView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RemediosSerializer
    def get_queryset(self):
        queryset = Remedios.objects.all()
        user = self.request.user
        return queryset.filter(email=user)

class RigidezView(ModelViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = RigidezSerializer
    def get_queryset(self):
        queryset = Rigidez.objects.all()
        user = self.request.user
        return queryset.filter(email=user)