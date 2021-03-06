from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from song.models import Song
from .models import FavoriteSong
from django.http import HttpResponse
import json

# Create your views here.
def add_remove_fav(request):

    user = request.user
    song_id = json.loads(request.body)['song-id']

    song_is_found = ''

    try:
        song_is_found = Song.objects.get(id=song_id)
        print('song found')
    except ObjectDoesNotExist:
        song_is_found = None
        print('Song is not found')

    if song_is_found:
        song_is_fav = ''

        try:
            song_is_fav = FavoriteSong.objects.get(user_fk=user, song_fk=song_is_found)
        except ObjectDoesNotExist:
            song_is_fav = None

        if song_is_fav:
            song_is_fav.delete()
        else:
            FavoriteSong.objects.create(user_fk=user, song_fk=song_is_found)
    else:
        print('error')

    return HttpResponse('<h1>hi</h1>')



