from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.viewsets import ModelViewSet
from .serializers import  DorSerializer, HumorSerializer, RemediosSerializer, RigidezSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Dor, Humor, Remedios, Rigidez


class DorView(ModelViewSet):
    queryset = Dor.objects.all()          
    serializer_class = DorSerializer

class HumorView(ModelViewSet):
    queryset = Humor.objects.all()          
    serializer_class = HumorSerializer

class RemediosView(ModelViewSet):
    queryset = Remedios.objects.all()          
    serializer_class = RemediosSerializer

class RigidezView(ModelViewSet):
    queryset = Rigidez.objects.all()          
    serializer_class = RigidezSerializer