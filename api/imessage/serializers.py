from rest_framework import serializers
from .models import *
from .fields import *
from .filters import *

class CustomUserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(
    #     required=True
    # )
    # username = serializers.CharField()
    # password = serializers.CharField(min_length=8, write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'username', 'password', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)  # as long as the fields are the same, we can just use this
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class FriendRequestSerializer(serializers.ModelSerializer):
    user = UserField(queryset=CustomUser.objects.all())
    requestedUser = UserField(queryset=CustomUser.objects.all())

    class Meta:
        model = FriendRequest
        fields = (
            'user',
            'requestedUser',
            'status'
        ) 

    

class ChatSerializer(serializers.ModelSerializer):
    user = UserField(many=True, queryset=CustomUser.objects.all())
    class Meta:
        model = Chat
        fields = '__all__'





class MessageSerializer(serializers.ModelSerializer):
    user = UserField(queryset=CustomUser.objects.all())
    chat = ChatField(queryset=Chat.objects.all())
    class Meta:
        model = Message
        fields = "__all__"

class User_ChatSerializer(serializers.ModelSerializer):
    user = UserField(queryset=CustomUser.objects.all())
    chat = ChatField(queryset=Chat.objects.all())
    meta = User_Chat
    fields = "__all__"
