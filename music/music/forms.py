from django.forms import ModelForm, ClearableFileInput, HiddenInput
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
            'audio_waveform_data': HiddenInput(),
        }
        exclude = ('artist',)