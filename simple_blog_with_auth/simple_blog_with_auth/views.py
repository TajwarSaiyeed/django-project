from django.shortcuts import render
from posts.models import Post


def home(request):
    featured_posts = Post.objects.all()
    return render(request, 'index.html', {
        'featured_posts': featured_posts
    })