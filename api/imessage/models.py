from django.db import models
from django.db.models import IntegerField, Model
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    birthday = models.DateField(null=True)

    def __str__(self):
        return self.username

class Message(models.Model):
    text = models.TextField(null=False)
    timestamp = models.TimeField(null=True)
    user_id = models.ForeignKey('CustomUser', on_delete=models.PROTECT, null=True, blank=True)