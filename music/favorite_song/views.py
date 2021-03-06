from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from song.models import Song
from .models import FavoriteSong
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
import json

# Create your views here.
def add_remove_fav(request):

    user = request.user
    song_id = json.loads(request.body)['song-id']

    if user.is_authenticated:

        song_is_found = ''

        # try to find the requested song
        try:
            song_is_found = Song.objects.get(id=song_id)
        except ObjectDoesNotExist:
            song_is_found = None

        # If song is found go ahead
        if song_is_found:
            song_is_fav = ''

            # Check if the song is already a favorite of the current user
            try:
                song_is_fav = FavoriteSong.objects.get(user_fk=user, song_fk=song_is_found)
            except ObjectDoesNotExist:
                song_is_fav = None

            # If the song is already a favorite of the user, remove it from his favorite list, else add it to the fav list
            if song_is_fav:
                song_is_fav.delete()
                return JsonResponse({'message': 'Song removed from favorites.'})
            else:
                FavoriteSong.objects.create(user_fk=user, song_fk=song_is_found)
                return JsonResponse({'message': 'Song added to favorites.'})

        # If the song is not found inform the user about it
        else:
            return JsonResponse({'message':'Shitti'})


        return JsonResponse({'message': 'Please Sanler.'})
    else:
        return JsonResponse({'message':'Please register.'})
