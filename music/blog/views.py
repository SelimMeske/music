from django.shortcuts import render
from django.http import HttpResponse
from music.forms import CustomBlogPostForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def create_blog_post(request):

    form = CustomBlogPostForm()
    return render(request, 'blog/create-post.html', {'form': form})