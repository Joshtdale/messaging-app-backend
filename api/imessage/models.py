from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import AbstractUser
import pusher

# pusher_client = pusher.Pusher(
#     app_id=u'1518560',
#     key=u'1fb64f027f5f40e81a79',
#     secret=u'1785068556fa75087922',
#     cluster=u'us2'
# )

# pusher_client.trigger(u'my-channel', u'my-event', {u'message': u'hello world'})

class CustomUser(AbstractUser):
    # birthday = models.DateField(null=True)
    extra_kwargs = {'password': {'write_only': True}}

    def __str__(self):
        return self.username

class Chat(models.Model):
    name = models.CharField(max_length=20, null=False)
    user = models.ManyToManyField('CustomUser')

class User_Chat(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.PROTECT, null=False)
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=False)

class Message(models.Model):
    text = models.TextField(null=False)
    timestamp = models.CharField(max_length=30,null=True)
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, blank=True)
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, null=True)

class FriendRequest(models.Model):
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True)
    requestedUser = models.ForeignKey('CustomUser',related_name='+' , on_delete=models.PROTECT, null=True)
    status = models.IntegerField(default=0)
