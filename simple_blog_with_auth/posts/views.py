from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from posts.forms import PostForm
from posts.models import Post


@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            messages.success(request, 'Post added successfully')
            return redirect('add_post')
    else:
        post_form = PostForm()
    return render(request, 'add-post.html', {
        'post_form': post_form
    })


@login_required
def edit_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        return redirect('index')
    post_form = PostForm(instance=post)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.instance.author = request.user
            post_form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('index')

    return render(request, 'add-post.html', {
        'post_form': post_form
    })


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        return redirect('index')
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('index')
