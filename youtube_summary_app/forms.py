
from django import forms

class VideoURLForm(forms.Form):
    video_url = forms.CharField(label='Video URL', max_length=200)