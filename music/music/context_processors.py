from user_profile.models import UserProfile

def user_info(request):

    if request.user.is_authenticated:
        user = request.user
        user_info = UserProfile.objects.all().filter(user_fk=user)
        print(user_info[0].is_artist)
        return {'userinfo': user_info[0]}

    return {'userinfo': ''}