from django.db import models

class Genre(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
       return self.title

class Music(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    genre = models.ForeignKey(Genre, on_delete = models.PROTECT)
    file = models.FileField(upload_to="media/music")
    music_text = models.TextField()
    def __str__(self):
        return self.title