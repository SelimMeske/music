from django.db import models
from django.conf import settings

# Create your models here.
class Song(models.Model):

    name = models.CharField(max_length=420)
    image = models.ImageField(upload_to='images/')
    audio = models.FileField(upolad_to='audio/')
    artist = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name