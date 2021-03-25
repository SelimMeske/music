from django.forms import ModelForm, ClearableFileInput, Textarea
from django import forms
from song.models import Song

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