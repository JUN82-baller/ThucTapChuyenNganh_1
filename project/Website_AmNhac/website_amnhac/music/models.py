from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='artist', blank=True, null=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    cover = models.ImageField(upload_to='albums', blank=True, null=True)
    release_year = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.title} - {self.artist.name}"


class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    audio_file = models.FileField(upload_to='songs', blank=True, null=True)
    duration = models.CharField(max_length=10, blank=True)  # duration of audio

    def __str__(self):
        return self.title
