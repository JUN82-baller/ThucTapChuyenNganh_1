import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Y_music_backend.settings')
django.setup()

from api.models import Song
from django.core.files import File

# Danh sách bài hát cần import
songs_to_import = [
    {
        'title': 'When Did You Get Hot',
        'artist': 'Sabrina Carpenter',
        'filename': 'Sabrina_Carpenter_-_When_Did_You_Get_Hot__Lyrics_online-audio-converter.com.mp3',
        'release_year': '2024'
    },
    {
        'title': 'Souvenir Remix',
        'artist': 'Selena Gomez',
        'filename': 'Selena_Gomez_-_Souvenir_Remix_feat._The_Weeknd.mp3',
        'release_year': '2024'
    }
]

media_path = os.path.join(os.path.dirname(__file__), 'media', 'songs')

for song_data in songs_to_import:
    file_path = os.path.join(media_path, song_data['filename'])
    
    if os.path.exists(file_path):
        # Kiểm tra xem bài hát đã tồn tại chưa
        if not Song.objects.filter(title=song_data['title'], artist=song_data['artist']).exists():
            # Tạo Song object
            song = Song(
                title=song_data['title'],
                artist=song_data['artist'],
                release_year=song_data['release_year']
            )
            
            # Gán file audio
            with open(file_path, 'rb') as f:
                song.audio_file.save(song_data['filename'], File(f), save=False)
            
            song.save()
            print(f"[OK] Added: {song_data['title']} by {song_data['artist']}")
        else:
            print(f"[SKIP] Already exists: {song_data['title']} by {song_data['artist']}")
    else:
        print(f"[ERROR] File not found: {file_path}")

print(f"\nTotal songs in database: {Song.objects.count()}")

