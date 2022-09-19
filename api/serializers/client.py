from django.db.models import fields
from rest_framework import serializers
from ..models.client import Client
  
class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('user_name', 'email', 'password')

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('email', 'password')