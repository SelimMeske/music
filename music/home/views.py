from django.shortcuts import render
from song.models import Song

# Create your views here.

def home_view(request):

    songs = Song.objects.all()

    return render(request, 'home/home.html', {'songs': songs})
