from django.apps import AppConfig


class ImessageConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'imessage'

    def ready(self):
        import imessage.signals