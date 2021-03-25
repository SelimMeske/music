from django.shortcuts import render, redirect
from music.forms import CustomUploadForm
from user_profile.models import UserProfile
from song.models import Song
import json
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse


# Create your views here.
def create_song(request):

    user = request.user

    # user_is_artist = True if UserProfile.objects.get(user_fk=user).is_artist else False

    # if not user_is_artist:
        # return redirect('home')
    if not user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        form = CustomUploadForm(request.POST, request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.artist = request.user
            post.save()
            return redirect('home')
        else:
            form = CustomUploadForm()
    form = CustomUploadForm()

    return render(request, 'create_song/create_song.html', {'form': form})

def delete_song(request):

    user = request.user
    if user.is_authenticated:
        song_id = json.loads(request.body)['song-id']
        try:
            Song.objects.get(id=song_id).delete()
        except ObjectDoesNotExist:
            return JsonResponse({'message':'There is an error occured.'})

        return JsonResponse({'message': 'Song deleted.'})

