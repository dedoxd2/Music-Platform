from django import forms
from .models import Album


class AlbumForm (forms.ModelForm):
    is_approved = forms.BooleanField(
        help_text="Approve the album if its name is not explicit", required=False)  # To Avoid Changing the field itself

    release_datetime = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),)

    # release_datetime = forms.DateTimeField(
    #     widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    # )

    class Meta:
        model = Album
        fields = ['name', 'cost', 'release_datetime', 'artist']
