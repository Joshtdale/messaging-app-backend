# Generated by Django 4.1.3 on 2022-12-05 22:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imessage', '0012_friendrequests'),
    ]

    operations = [
        migrations.AddField(
            model_name='friendrequests',
            name='requester',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]