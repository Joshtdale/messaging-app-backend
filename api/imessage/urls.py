from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

router = routers.SimpleRouter()
router.register(r'customuser', CustomUserViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'chats', ChatViewSet)
router.register(r'friends', FriendRequestViewSet)
# router.register(r'messages/pusher', push_feed)




urlpatterns = [
    path('', include(router.urls)),
    path('user/signup/', UserCreate.as_view(), name="create_user"),
    path('users/<int:pk>/', UserDetail.as_view(), name="get_user_details"),
    path('user/login/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

]