from django.shortcuts import render
from song.models import Song
from favorite_song.models import FavoriteSong

# Create your views here.

def home_view(request):

    songs = Song.objects.all()
    favorite_songs = {}

    if request.user.is_authenticated:
        favorite_songs = FavoriteSong.objects.all().filter(user_fk=request.user)

    return render(request, 'home/home.html', {'songs': songs, 'fav_songs': favorite_songs})
