# Generated by Django 5.0.6 on 2024-06-15 21:33

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0003_room_room_guid"),
    ]

    operations = [
        migrations.AddField(
            model_name="meeting",
            name="meeting_guid",
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
