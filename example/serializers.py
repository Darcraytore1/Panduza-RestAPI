from rest_framework import serializers
from .models import Device
from django.http import HttpResponseBadRequest

class DeviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ['id', 'name']

    def create(self, validated_data):
        if Device.objects.filter(**validated_data).exists():
            raise HttpResponseBadRequest('device already exists')
        return Device.objects.create(**validated_data)
