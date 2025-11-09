from django.db import models

# Create your models here.
class Song(models.Model):
    title= models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file= models.FileField(upload_to='songs/')
    album_cover = models.ImageField(upload_to='album_covers/', blank=True, null=True)
    release_year = models.CharField(max_length=4, blank=True, null=True)
    uploaded_at= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.artist}"
    
    class Meta:
        ordering = ['artist', 'id']
