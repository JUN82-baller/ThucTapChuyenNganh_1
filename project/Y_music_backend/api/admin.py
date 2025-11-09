from django.contrib import admin
from .models import Song
from django.utils.html import format_html
# Register your models here.
class SongAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'release_year', 'audio_player', 'uploaded_at')
    list_filter = ('artist', 'release_year')
    search_fields = ('title', 'artist')

    def audio_player(self, obj):
        if obj.audio_file:
            return format_html(
                f'<audio controls loop><source src="{obj.audio_file.url}" type="audio/mpeg">Your browser does not support the audio element.</audio>'
            )
        return "No audio file"
    audio_player.short_description = "Audio Player"
admin.site.register(Song, SongAdmin)
