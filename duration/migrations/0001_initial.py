# Generated by Django 4.2.3 on 2023-09-04 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Playlist_items_Id",
            fields=[
                (
                    "playlist_Id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("channel_Name", models.CharField(max_length=100)),
                ("num_of_videos", models.IntegerField()),
                ("channel_id", models.CharField(max_length=200)),
            ],
        ),
    ]
