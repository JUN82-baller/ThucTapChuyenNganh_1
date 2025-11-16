from django.urls import path
from . import views

urlpatterns = [
    path('albums/', views.albums_store, name='albums'),
]
