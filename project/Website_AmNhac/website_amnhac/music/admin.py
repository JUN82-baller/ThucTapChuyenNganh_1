from django.contrib import admin
from .models import Artist, Album, Song
# Register your models here.
@admin.register(Artist)
class ArtistAdmid(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year', 'price')
    list_filter = ('release_year','artist')
    search_fields = ('tile',)

@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    list_display = ('title','album', 'duration')
    search_fields = ('title',)

