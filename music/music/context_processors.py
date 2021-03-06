from user_profile.models import UserProfile
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

def user_info(request):

    if request.user.is_authenticated:
        user = request.user
        is_user_there = UserProfile.objects.all().filter(user_fk=user)

        if is_user_there:
            return {'userinfo': is_user_there[0]}
        else:
            return {'userinfo': ''}

    return {'userinfo': ''}