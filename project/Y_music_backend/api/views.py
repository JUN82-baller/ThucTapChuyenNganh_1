from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from .serializers import SongSerializer

# Template view
def song_list(request):
    songs = Song.objects.all()
    return render(request, 'api/song_list.html', {'songs': songs})

# API views
class SongViewSet(viewsets.ModelViewSet):
    queryset = Song.objects.all().order_by('id')
    serializer_class = SongSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

@api_view(['GET'])
def songs_list_api(request):
    """
    API endpoint để lấy danh sách bài hát
    """
    songs = Song.objects.all().order_by('id')
    serializer = SongSerializer(songs, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def songs_grouped_by_artist(request):
    """
    API endpoint để lấy danh sách bài hát được nhóm theo artist
    """
    songs = Song.objects.all().order_by('artist', 'id')
    artists_dict = {}

    for song in songs:
        artist_name = song.artist
        if artist_name not in artists_dict:
            album_cover_url = '/images/albumCovers/default.png'
            if song.album_cover:
                album_cover_url = request.build_absolute_uri(song.album_cover.url)
            elif songs.filter(artist=artist_name, album_cover__isnull=False).exists():
                first_song_with_cover = songs.filter(artist=artist_name, album_cover__isnull=False).first()
                album_cover_url = request.build_absolute_uri(first_song_with_cover.album_cover.url)

            release_year = song.release_year if song.release_year else None

            artists_dict[artist_name] = {
                'name': artist_name,
                'albumCover': album_cover_url,
                'releaseYear': release_year,
                'tracks': []
            }

        artists_dict[artist_name]['tracks'].append({
            'id': song.id,
            'name': song.title,
            'path': request.build_absolute_uri(song.audio_file.url) if song.audio_file else None
        })

    artists_list = list(artists_dict.values())
    return Response(artists_list)

@api_view(['POST'])
def bulk_create_songs(request):
    """
    Nhận danh sách bài hát và lưu hàng loạt
    """
    serializer = SongSerializer(data=request.data, many=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
