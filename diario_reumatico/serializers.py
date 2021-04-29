from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Dor, Humor, Remedios, Rigidez
from django.contrib.auth import get_user_model

class DorSerializer(ModelSerializer):
    class Meta:
        model = Dor
        fields = ('__all__')

class HumorSerializer(ModelSerializer):
    class Meta:
        model = Humor
        fields = ('__all__')


class RemediosSerializer(ModelSerializer):
    class Meta:
        model = Remedios
        fields = ('__all__')

class RigidezSerializer(ModelSerializer):
    class Meta:
        model = Rigidez
        fields = ('__all__')