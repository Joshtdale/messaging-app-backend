from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

class Chat(models.Model):
    name = models.CharField(max_length=15, null=False)

# class User_Chat(models.Model):
#     user = m

class Message(models.Model):
    text = models.TextField(null=False)
    timestamp = models.CharField(max_length=30,null=True)
    user = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, blank=True)
    chat = models.ForeignKey('Chat', on_delete=models.PROTECT, null=True)