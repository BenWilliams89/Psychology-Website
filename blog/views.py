from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'home.html', {})


class PostList(ListView):
    queryset = Post.objects.all()
    template_name = "blog.html"
    paginate_by = 6



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
    form_class = PostForm
    template_name = 'update_post.html'
    #fields = '__all__'




class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog.html')



class CommentAdd(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    success_url = reverse_lazy('blog.html')