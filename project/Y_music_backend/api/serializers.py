from rest_framework import serializers
from .models import Song


class SongSerializer(serializers.ModelSerializer):
    audio_file_url = serializers.SerializerMethodField()
    album_cover_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'audio_file_url', 'album_cover_url', 'release_year', 'uploaded_at']
        read_only_fields = ['id', 'uploaded_at']
    
    def get_audio_file_url(self, obj):
        if obj.audio_file:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.audio_file.url)
            return obj.audio_file.url
        return None
    
    def get_album_cover_url(self, obj):
        if obj.album_cover:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.album_cover.url)
            return obj.album_cover.url
        return None
