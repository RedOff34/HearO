from django.db import models
from SignIn.models import User
from rest_framework import serializers
# Create your models here.

class DeviceTokenSerializer(serializers.Serializer):
    device_token = serializers.CharField(max_length=500)

class Location(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True) 


class danger(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    danger_type = models.CharField(max_length=50)
    soundfile = models.CharField(max_length=500)
    prob = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    