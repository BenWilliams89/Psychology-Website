from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .models import Post
from .forms import PostForm
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "blog.html"
    paginate_by = 6


def post_detail(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "post_detail.html",
        {"post": post},
    )