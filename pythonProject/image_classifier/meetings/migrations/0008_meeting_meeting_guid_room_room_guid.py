# Generated by Django 5.0.6 on 2024-06-15 21:37

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0007_remove_room_room_guid"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="meeting_guid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
        migrations.AddField(
            model_name="room",
            name="room_guid",
            field=models.UUIDField(default=uuid.uuid4, unique=True),
        ),
    ]