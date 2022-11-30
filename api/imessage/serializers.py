from rest_framework import serializers
from .models import *
from .fields import *

class CustomUserSerializer(serializers.ModelSerializer):
    # some_relationship_fk = SomeRelationshipSerializer(required=False)   
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
            'first_name',
            
    ) 

class ChatSerializer(serializers.ModelSerializer):

    class Meta:
        model = Chat
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    user = UserField(queryset=CustomUser.objects.all())
    chat = ChatField(queryset=Chat.objects.all())
    class Meta:
        model = Message
        fields = "__all__"
