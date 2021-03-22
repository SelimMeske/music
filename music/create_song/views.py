from django.shortcuts import render, redirect
from music.forms import CustomUploadForm
from user_profile.models import UserProfile


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
