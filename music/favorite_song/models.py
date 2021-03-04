from django.db import models
from django.conf import settings
from song.models import Song

# Create your models here.
class FavoriteSong(models.Model):

    user_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    song_fk = models.ForeignKey(
        Song,
        on_delete=models.CASCADE
    )