from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from car.models import Car
from order.models import Order
from django.contrib import messages

@login_required
def place_my_order(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if car.quantity > 0:
        Order.objects.create(car=car, user=request.user)
        car.quantity -= 1
        car.save()
        messages.success(request, f'You have successfully purchased {car.name}.')
        return redirect('profile')
    else:
        messages.error(request, 'Sorry, this car is out of stock')
        return redirect('car_detail', pk=pk)
