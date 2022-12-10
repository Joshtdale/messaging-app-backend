from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from rest_framework import status, permissions, generics, filters
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from pusher import pusher_client, Pusher

# from .serializers import CustomUserSerializer

class UserCreate(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request, format='json'):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetail(generics.RetrieveAPIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MessageViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer
    http_method_names = ['get','post','put','delete']
    
    def post(self, request):
        obj = Messages.objects.filter(is_deleted=False,parent=None).order_by('-timestamp')[:10]
        last_message = obj.last()
        print(request)
        pusher.trigger(
            'imclone_channel', 
            "chat_group_" + request.chat.id, 
        {
            
            "id": last_message.id,
            "text": request.text,
            "user": {
                "id": request.user.id,
                "name": request.user.name
            },
            "timestamp": last_message.timestamp,
            "chat": {
                "id": request.chat.id,
                "name": request.chat.name
            }
        }
            
        )
        return Response([])


    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    

class ChatViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer


    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        pusher_client = pusher.Pusher(
            app_id=u'1518560', 
            key=u'1fb64f027f5f40e81a79', 
            secret=u'1785068556fa75087922', 
            cluster=u'us2'
        )
        pusher.trigger(
            'imclone_channel', 
            "chat_group_" + chat_id, 
        {
            "message": {
                "id": idTime,
                'text': message_body,
                "user": {
                        "id": posted_by_id
                        },
                'chat': {
                    chat_id
                }
            }
        }
        # "timestamp": idTime
        # 'posted_by': posted_by_id,
        )


class FriendRequestViewSet(ModelViewSet):
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)