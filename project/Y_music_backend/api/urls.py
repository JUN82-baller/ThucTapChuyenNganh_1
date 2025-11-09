from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router cho ViewSet
router = DefaultRouter()
router.register(r'songs', views.SongViewSet, basename='song')

urlpatterns = [
    # Template view (Django template)
    path('', views.song_list, name='song_list'),
    
    # API endpoints
    path('api/', include(router.urls)),
    path('api/songs/list/', views.songs_list_api, name='songs_list_api'),
    path('api/songs/grouped/', views.songs_grouped_by_artist, name='songs_grouped_by_artist'),
    path('songs/bulk/', views.bulk_create_songs),
]

