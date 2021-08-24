from django.urls import path, include
from .views import SingleSongView, SongView

urlpatterns = [
    path('songs', SongView.as_view()),
    path('song-by-id', SingleSongView.as_view())
]