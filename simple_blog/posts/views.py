from django.shortcuts import render, redirect

from posts.forms import PostForm
from posts.models import Post


# Create your views here.
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request, 'add_post.html', {
        'post_form': post_form
    })


def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('index')

    return render(request, 'add_post.html', {
        'post_form': post_form
    })

def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    post.delete()
    return redirect('index')
