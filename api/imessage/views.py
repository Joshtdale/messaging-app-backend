from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from .models import *
from .serializers import *
from rest_framework.response import Response

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MessageViewSet(ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
