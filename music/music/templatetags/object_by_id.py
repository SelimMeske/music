from django import template
from django.core.exceptions import ObjectDoesNotExist
from favorite_song.models import FavoriteSong

register = template.Library()

@register.filter(name='object_by_id')
def get_by_id(value, arg):


    if arg.is_authenticated:
        try:
            fav_song = FavoriteSong.objects.get(user_fk=arg, song_fk=value)
            return 'fav-btn favourite-song'
        except ObjectDoesNotExist:
            return 'fav-btn'
    else:
        return 'fav-btn'