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
            'audio_waveform_data'
        )
        widgets = {
            'audio_waveform_data': Textarea(),
        }
        exclude = ('artist',)