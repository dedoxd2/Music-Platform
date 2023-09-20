from django.contrib import admin
from .models import Album
from .forms import AlbumForm
# Register your models here.


@admin.action(description='Mark selected Albums as published')
def make_published(modeladmin, request, queryset):
    queryset.update(is_approved=True)


class AlbumAdmin(admin.ModelAdmin):
    list_display = ['name', 'creation_datetime',
                    'release_datetime', 'cost', 'artist', 'is_approved']
    list_editable = ['is_approved']
    readonly_fields = ['creation_datetime',]
    actions = [make_published]
    form = AlbumForm


# admin.site.unregister(Album,AlbumAdmin)
admin.site.register(Album, AlbumAdmin)
