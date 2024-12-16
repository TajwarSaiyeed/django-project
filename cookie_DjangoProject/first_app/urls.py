from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('', views.set_session, name='index'),
    path('get_session/', views.get_session, name='index'),
    path('del_session/', views.delete_session, name='index'),
    path('get_cookie/', views.get_cookie, name='get_cookie'),
    path('del_cookie/', views.delete_cookie, name='del_cookie'),
]
