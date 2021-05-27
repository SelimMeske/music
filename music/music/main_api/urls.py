from django.urls import path, include
from .views import SongView

urlpatterns = [
    path('songs', SongView.as_view())
]