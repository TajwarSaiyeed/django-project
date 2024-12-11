from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

from posts.forms import PostForm, CommentForm
from posts.models import Post

from django.views.generic import CreateView, UpdateView, DeleteView, DetailView


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
        'form': post_form
    })


# add post using class based view
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    success_url = reverse_lazy('add_post')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, 'Post added successfully')
        return super().form_valid(form)


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
        'form': post_form
    })


# edit post using class based view
@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'add-post.html'
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'post_id'

    def form_valid(self, form):
        if form.instance.author != self.request.user:
            return redirect('index')
        messages.success(self.request, 'Post updated successfully')
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_details.html'
    pk_url_kwarg = 'post_id'

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post_ = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post_
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        comment_form = CommentForm(data=self.request.POST)
        context['comment_form'] = comment_form
        return context


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post.author != request.user:
        return redirect('index')
    post.delete()
    messages.success(request, 'Post deleted successfully')
    return redirect('index')


# Delete post using class based view
@method_decorator(login_required, name='dispatch')
class DeletePostView(DeleteView):
    model = Post
    success_url = reverse_lazy('index')
    pk_url_kwarg = 'post_id'
    template_name = 'delete_post.html'
