# Generated by Django 4.2.3 on 2023-09-04 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("duration", "0002_rename_playlist_items_id_playlist_id_playlist_items"),
    ]

    operations = [
        migrations.AddField(
            model_name="playlist_items",
            name="video_published",
            field=models.CharField(default="1 year ago", max_length=100),
        ),
    ]