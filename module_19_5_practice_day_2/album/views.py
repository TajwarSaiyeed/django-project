from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.decorators import login_required

from .models import Album
from .forms import AlbumForm


@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        return super().form_valid(form)
