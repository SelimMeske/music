from django.forms import ModelForm
from django import forms
from song.models import Song

class CustomUploadForm(ModelForm):

    class Meta:
        model = Song
        fields = [
            'name',
            'image',
            'audio'
        ]
        exclude = ('artist',)