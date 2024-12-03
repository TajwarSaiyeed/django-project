from django.shortcuts import render
from posts.models import Post
from categories.models import Category


def home(request, slug=None):
    featured_posts = slug and Post.objects.filter(category__slug=slug) or Post.objects.all()
    categories = Category.objects.all()
    return render(request, 'index.html', {
        'featured_posts': featured_posts,
        'categories': categories
    })
