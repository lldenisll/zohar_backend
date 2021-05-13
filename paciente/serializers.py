from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import MyUser

class MyUserSerializer(ModelSerializer):
    class Meta:
        model = MyUser
        fields = ('__all__')

