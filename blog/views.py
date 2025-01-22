from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
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


#def post_detail(request, slug):
 #   queryset = Post.objects.filter(status=1)
 #   post = get_object_or_404(queryset, slug=slug)

 #  return render(
  #      request,
   #     "post_detail.html",
   #     {"post": post},
   # )

class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'



class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'



class UpdatePostView(UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = '__all__'