from django.urls import path

from categories import views

from simple_blog_with_auth.views import home

urlpatterns = [
    path('add/', views.add_category, name="add_category"),
    path('category/<slug:slug>/', home, name="category_slug"),
]