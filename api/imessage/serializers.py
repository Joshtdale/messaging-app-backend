from rest_framework import serializers
from .models import *

class CustomUserSerializer(serializers.ModelSerializer):

    class Meta:
        model= CustomUser
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    user_id = CustomUserSerializer()
    class Meta:
        model = Message
        fields = "__all__"
