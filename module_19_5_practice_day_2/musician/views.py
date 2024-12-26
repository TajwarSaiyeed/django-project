from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import Musician
from .forms import MusicianForm


@method_decorator(login_required, name='dispatch')
class AddMusicianView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class EditMusiciansView(UpdateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class DeleteMusicianView(DeleteView):
    model = Musician
    template_name = 'delete_musician.html'
    success_url = reverse_lazy('home')
    pk_url_kwarg = 'pk'
