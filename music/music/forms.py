from django.forms import ModelForm, ClearableFileInput
from django import forms
from song.models import Song

class CustomUploadForm(ModelForm):

    class Meta:
        model = Song
        fields = (
            'name',
            'image',
            'audio'
        )
        widgets = {
            'audio': ClearableFileInput(attrs={'onchange': 'on_change()'}),
        }
        exclude = ('artist',)