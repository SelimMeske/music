from django.db import models
from datetime import datetime

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    published = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.title