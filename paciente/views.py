from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import  MyUserSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import MyUser
from rest_framework.permissions import IsAuthenticated


class MyUserView(ModelViewSet):
    permission_classes = (IsAuthenticated,)  
    serializer_class = MyUserSerializer
    def get_queryset(self):
        queryset = MyUser.objects.all()
        user = self.request.user
        return queryset.filter(email=user)