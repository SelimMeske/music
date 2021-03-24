from django.forms import ModelForm, FileField
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
        widgets = {
            'audio': FileField(attrs={'onchange': 'onChange()'})
        }
        exclude = ('artist',)