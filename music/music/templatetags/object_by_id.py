from django import template
from django.core.exceptions import ObjectDoesNotExist
from favorite_song.models import FavoriteSong

register = template.Library()

@register.filter(name='object_by_id')
def get_by_id(value, arg):


    if arg.is_authenticated:
        print('is')
        try:
            fav_song = FavoriteSong.objects.get(user_fk=arg, song_fk=value)
            print('is favor')
            return 'fav-btn favourite-song'
        except ObjectDoesNotExist:
            print('is not favor')
            return 'fav-btn'
    else:
        return 'fav-btn'