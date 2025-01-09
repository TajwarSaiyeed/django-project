from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin

from car.models import Car
from car_brand.models import CarBrand
from comment.forms import CommentForm

class CarListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'cars'

    def get_queryset(self):
        queryset = super().get_queryset()
        brand_name = self.request.GET.get('brand')
        if brand_name:
            queryset = queryset.filter(car_brand__name=brand_name)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] = CarBrand.objects.all()
        context['selected_brand'] = self.request.GET.get('brand', '')
        return context



class CarDetailView(FormMixin, DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['comments'] = self.object.comments.all()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            comment = form.save(commit=False)
            comment.car = self.object
            comment.save()
            return redirect('car_detail', pk=self.object.pk)
        return self.form_invalid(form)