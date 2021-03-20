from django.shortcuts import render
from song.models import Song
from django.core.serializers import serialize
import json

# Create your views here.
def profile_view(request):

    user = request.user

    if user.is_authenticated:
        songs = Song.objects.all().filter(artist=user)
        serialized_songs = serialize('json', songs, ensure_ascii=False)
    else:
        songs = ''

    return render(request, 'profile/my_profile.html', {'songs': songs, 'ser_songs': json.dumps(serialized_songs)})