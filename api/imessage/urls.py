from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'customuser', CustomUserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'chats', ChatViewSet)


urlpatterns = [
    path('', include(router.urls)),

]