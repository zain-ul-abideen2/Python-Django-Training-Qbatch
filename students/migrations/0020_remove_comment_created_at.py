# Generated by Django 4.2.15 on 2024-08-28 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0019_comment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="created_at",
        ),
    ]
