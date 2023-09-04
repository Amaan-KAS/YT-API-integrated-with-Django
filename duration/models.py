from django.db import models

# Create your models here.
class Playlist_Id(models.Model):
    playlist_Id = models.CharField(max_length=200,blank=False, primary_key=True)
    channel_Name = models.CharField(max_length=100)
    num_of_videos = models.IntegerField()
    channel_id = models.CharField(max_length=200)
    def __str__(self):
        return self.playlist_Id

class Playlist_items(models.Model):
    playlist_Id = models.ForeignKey(Playlist_Id, 
                                    on_delete=models.PROTECT,
                                    blank=False)
    video_Id = models.CharField(max_length=200,blank=False, primary_key=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=1000, blank=True, null=True)
    thumbnail = models.CharField(max_length=240)
    video_published = models.CharField(max_length=100, default="1 year ago")
    def __str__(self):
        return self.title
    


    