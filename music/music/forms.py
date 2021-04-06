from django.forms import ModelForm, ClearableFileInput, Textarea
from django import forms
from song.models import Song
from blog.models import BlogPost
from tinymce.widgets import TinyMCE

class CustomUploadForm(ModelForm):

    class Meta:
        model = Song
        fields = (
            'name',
            'image',
            'audio',
            'audio_data'
        )
        widgets = {
            'audio_data': Textarea()
        }
        exclude = ('artist',)

class CustomBlogPostForm(ModelForm):

    class Meta:
        model = BlogPost
        fields = (
            'title',
            'content',
        )
        widget = {
            'content': TinyMCE(attrs={'cols':80, 'rows': 30})
        }
