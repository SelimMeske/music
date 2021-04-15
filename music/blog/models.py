from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = RichTextField(blank=True, null=True)
    published = models.DateTimeField(default=datetime.now, blank=False)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title