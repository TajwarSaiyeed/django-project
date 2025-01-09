

from django.urls import path

from car.views import CarDetailView
from order.views import place_my_order


urlpatterns = [
     path('<int:pk>/', CarDetailView.as_view(), name='car_detail'),
     path('<int:pk>/buy', place_my_order, name='place_my_order'),
]