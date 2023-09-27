from typing import Any
from django.shortcuts import render
from .models import *
from .forms import ArtistForm
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class ArtistFormView(LoginRequiredMixin, FormView):
    template_name = "artists/artist_form.html"
    form_class = ArtistForm
    # Redirect to artist list after form is successfully submitted
    success_url = reverse_lazy('artist_list')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['ArtistForm'] = context.pop('form')

        return context


class ArtistListView(ListView):
    model = Artist
    template_name = 'artists/artist_list.html'
    context_object_name = 'list'

    def get_queryset(self):

        return Artist.objects.prefetch_related('albums')


# def artist_form(request):
#     if request.method == "POST":
#         form = ArtistForm(request.POST)
#         if form.is_valid():
#             form.save()
#     else:
#         form = ArtistForm()

#     return render(request, 'artists/artist_form.html', {'ArtistForm': form})


# def artist_list(request):
#     artists_list = Artist.objects.prefetch_related('albums')

#     return render(request, 'artists/artist_list.html', {'list': artists_list})
