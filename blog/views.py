from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from .models import Post, PostForm, Tag


class PostList(generic.ListView):
    # queryset = Post.objects.filter(status=2).order_by('date_created')
    model = Post
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.filter(status=2).order_by('-date_created')
        context['tags'] = Tag.objects.all().order_by('title')
        context['form'] = PostForm()
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'


# @login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('/')


def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('/')


def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = PostForm(instance=post)
        return render(request, 'edit.html', {'form': form})
