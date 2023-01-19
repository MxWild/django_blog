from django.views import generic

from blog.models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('date_created')
    template_name = 'index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
