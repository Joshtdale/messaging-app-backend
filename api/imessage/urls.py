from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'customuser', CustomUserViewSet)
router.register(r'messages', MessageViewSet)
# router.register(r'chats', ChatViewSet, basename='Chat')
router.register(r'friends', FriendRequestViewSet)
router.register(r'userchat', User_ChatViewSet)

# router.register(r'chats', viewset)
# router.register(r'messages/pusher', push_feed)




urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('chats/<int:pk>/', ChatViewSet.as_view({'get': 'list'}), name="get_chat_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    # path('chats/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]