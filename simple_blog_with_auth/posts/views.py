from django.shortcuts import render, redirect
from django.contrib import messages
from posts.forms import PostForm
from posts.models import Post


def add_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post added successfully')
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request, 'add-post.html', {
        'post_form': post_form
    })


def edit_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')

    post = Post.objects.get(pk=post_id)
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('index')

    return render(request, 'add-post.html', {
        'post_form': post_form
    })


def delete_post(request, post_id):
    if not request.user.is_authenticated:
        return redirect('login')
    post = Post.objects.get(pk=post_id)
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('index')
