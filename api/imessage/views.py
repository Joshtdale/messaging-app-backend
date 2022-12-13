from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, mixins, ViewSet
from rest_framework import status, permissions, generics, filters
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from django_filters import Filter, filters
from .filters import *
from rest_framework import status, generics


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

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class UserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserViewSet(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class MessageViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    

class ChatViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    # queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filter'] = ChatFilter(self.request.GET)

    def get_queryset(self):
        queryset = Chat.objects.filter(user__id=self.request.user.id)
        return queryset


    # class ChatUserViewSet(ModelViewSet):
    #     permission_classes = (permissions.IsAuthenticated,)
    #     queryset = Chat.objects.all()
    #     # queryset = Chat.objects.filter(user__container=[13])
    #     serializer_class = ChatSerializer


    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class ChatUpdateViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)
    # def post(self, request, *args, **kwargs):
    #     pusher_client = pusher.Pusher(
    #         app_id=u'1518560', 
    #         key=u'1fb64f027f5f40e81a79', 
    #         secret=u'1785068556fa75087922', 
    #         cluster=u'us2'
    #     )
    #     pusher.trigger(
    #         'imclone_channel', 
    #         "chat_group_" + chat_id, 
    #     {
    #         "message": {
    #             "id": idTime,
    #             'text': message_body,
    #             "user": {
    #                     "id": posted_by_id
    #                     },
    #             'chat': {
    #                 chat_id
    #             }
    #         }
    #     }
    #     # "timestamp": idTime
    #     # 'posted_by': posted_by_id,
    #     )


class FriendRequestViewSet(ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = FriendRequest.objects.all()
    serializer_class = FriendRequestSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class User_ChatViewSet(ModelViewSet):
    queryset = User_Chat.objects.all()
    serializer_class = User_ChatSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)