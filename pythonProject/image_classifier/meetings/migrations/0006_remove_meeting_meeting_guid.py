# Generated by Django 5.0.6 on 2024-06-15 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("meetings", "0005_alter_meeting_meeting_guid"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="meeting",
            name="meeting_guid",
        ),
    ]
