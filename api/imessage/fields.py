from rest_framework import serializers
from .models import *

class UserField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = CustomUser.objects.get_or_create(**data)
        return obj
    def to_representation(self, value):
        return {
            "id": value.id,
            "name": value.username

        }

class ChatField(serializers.RelatedField):
    def to_internal_value(self, data):
        obj, created = Chat.objects.get_or_create(**data)
        return obj
    def to_representation(self, value):
        return {
            "id": value.id,
            "name": value.name

        }