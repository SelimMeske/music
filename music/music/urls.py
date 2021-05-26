from django.contrib import admin
from django.urls import path, include
from home import views as home_view
from userauth import views as auth_views
from user_profile import views as profile_view
from django.conf import settings
from django.conf.urls.static import static
from create_song import views as create_song_view
#from favorite_song import views as favorite_song_view
from blog import views as blog_views
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'test', views.SongViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
    #path('', home_view.home_view, name='home'),
    #path('register', auth_views.signup_view, name='register'),
    #path('login', auth_views.login_view, name='login'),
    #path('logout', auth_views.logout_view, name='logout'),
    #path('profile', profile_view.profile_view, name='profile'),
    #path('new-song/', create_song_view.create_song, name='create_song'),
    #path('add-remove-song', favorite_song_view.add_remove_fav, name='add_remove_fav'),
    #path('delete-song', create_song_view.delete_song, name='delete_song'),
    #path('create-post', blog_views.create_blog_post, name='create_post'),
    #path('get-all-posts', blog_views.get_all_blog_posts, name='get-posts'),
    #path('post/<int:pk>', blog_views.get_single_post, name='single-post')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
