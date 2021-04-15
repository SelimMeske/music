from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from music.forms import CustomBlogPostForm
from .models import BlogPost
from django.contrib.auth.decorators import login_required
from django.core import serializers
# Create your views here.
@login_required
def create_blog_post(request):

    if request.method == 'POST':
        form = CustomBlogPostForm(request.POST, request.FILES)

        print(form)

        if form.is_valid():
            form.save()
            print('prosla')
        else:
            form = CustomBlogPostForm()
            print('nije prosla')

    form = CustomBlogPostForm()
    return render(request, 'blog/create-post.html', {'form': form})

def get_all_blog_posts(request):

    try:
        all_blog_posts = BlogPost.objects.all()
    except(error):
        pass
    
    serial_response = serializers.serialize('json', all_blog_posts)
    return JsonResponse(serial_response, safe=False)