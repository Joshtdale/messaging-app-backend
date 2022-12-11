from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Message
from .serializers import MessageSerializer
import pusher

@receiver([post_save, ], sender=Message)
def notify_with_pusher(sender, instance, created, **kwargs):
    if created:
        serializer = MessageSerializer(instance)

        pusher_client = pusher.Pusher(
            app_id=u'1518560', 
            key=u'1fb64f027f5f40e81a79', 
            secret=u'1785068556fa75087922', 
            cluster=u'us2'
        )
        pusher_client.trigger(
            "imclone_channel", 
            "chat_group_" + str(instance.chat.id), 
            serializer.data
        )