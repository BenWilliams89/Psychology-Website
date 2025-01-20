from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Post
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = "website/blog.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "website/post_detail.html",
        {"post": post},
    )