from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'home.html', {})




class PostList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog.html"
    paginate_by = 6
    
    
def post_detail(self, request, title, author, content):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset)
    comment = post.comments.all().order_by("-created_on")
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if CommentForm.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html',
                {'post': post,
                'comments': comments,
                'comment': comment,
                'comment_form': comment_form})


#class PostDetail(DetailView):
 #   model = Post
  #  template_name = 'post_detail.html'
   # success_url = reverse_lazy('blog.html')
    #def get(self, request, post_id):
        #post = Post.objects.get(id=post_id)
        #comments = post.comments.all()
        #return render(request, 'post_detail.html', {'post': post, 'comments': comments})



class PostAdd(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('blog.html')



class UpdatePostView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'update_post.html'
    success_url = reverse_lazy('blog.html')




class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('blog.html')



class CommentAdd(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('blog.html')

    
    


class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'update_comment.html'
    success_url = reverse_lazy('blog.html')



class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('blog.html')


