from django.shortcuts import render
from .models import *
from .forms import AlbumForm

# Create your views here.


def album_form(request):

    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlbumForm()
    return render(request, 'albums/album_form.html', {'AlbumForm': AlbumForm})
