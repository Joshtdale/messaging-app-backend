# Generated by Django 4.1.3 on 2022-12-05 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imessage', '0013_friendrequests_requester'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friendrequests',
            old_name='requester',
            new_name='user',
        ),
    ]