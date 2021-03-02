from django.shortcuts import render, redirect
from music.forms import CustomUploadForm


# Create your views here.
def create_song(request):

    if request.method == "POST":
        form = CustomUploadForm(request.POST, request.FILES)
        print(request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.artist = request.user
            post.save()
            return redirect('home')
        else:
            form = CustomUploadForm()
    form = CustomUploadForm()

    return render(request, 'create_song/create_song.html', {'form': form})
