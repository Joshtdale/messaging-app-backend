# Generated by Django 4.1.3 on 2022-11-30 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imessage', '0007_message_chat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='timestamp',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
