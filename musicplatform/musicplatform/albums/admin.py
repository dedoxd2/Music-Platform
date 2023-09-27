from django.contrib import admin
from .models import Album, Song
from django import forms
from .forms import AlbumForm, SongForm
# Register your models here.


class SongINline (admin.TabularInline):
    model = Song
    extra = 1

    def clean(self):
        super().clean()
        songs = self.cleaned_data.get('songs')
        if not songs:
            raise forms.ValidationError(
                "An album must have at least one song.")


class AlbumInline (admin.TabularInline):
    model = Album
    extra = 1


@admin.action(description='Mark selected Albums as published')
def make_published(modeladmin, request, queryset):
    queryset.update(is_approved=True)


class AlbumAdmin(admin.ModelAdmin):
    def song_count(self, album):
        return album.songs.all().count()
    song_count.short_description = 'Number of songs'

    def songs(self, album):
        name_songs = []
        for song in album.songs.all():
            name_songs.append(song)
        return name_songs
    songs.short_description = "All Songs"

    list_display = ['name', 'creation_datetime',
                    'release_datetime', 'cost', 'artist', 'is_approved', 'songs', 'song_count']
    list_editable = ['is_approved']
    readonly_fields = ['creation_datetime',]
    actions = [make_published]
    form = AlbumForm
    inlines = [SongINline]


class SongAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'thumbnail', 'audio', 'album']
    form = SongForm


# admin.site.unregister(Album,AlbumAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Song, SongAdmin)
