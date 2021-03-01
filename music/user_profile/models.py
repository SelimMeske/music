from django.db import models
from django.conf import settings

# Create your models here.
class UserProfile(models.Model):

    user_fk = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    user_name = models.CharField(max_length=500)
    profile_image = models.ImageField(null=True)
    description = models.CharField(max_length=10000)

    def __str__(self):
        return self.user_name
