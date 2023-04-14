from rest_framework import serializers

from .models import Hub,HubRegister


class HubSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hub
        fields = '__all__'



class HubRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = HubRegister
        fields = ['hub', 'user']

   