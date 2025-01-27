from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.urls import reverse, reverse_lazy
# Create your views here.


def home(request):
    return render(request, 'home.html', {})




class PostList(ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog.html"
    paginate_by = 6
    
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk, status=1)
    comments = post.comments.all().order_by("-created_on")
    comment = None
    print('one')

    if request.method == 'POST':
        print('2')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            print('3')
            comment = comment_form.save(commit=False)
            print('4')
            comment.author = request.user
            comment.post = post
            print(comment.author)
            comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {
        'post': post,
        'comments': comments,
        'comment': comment,
        'comment_form': comment_form,
    })


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

    def form_valid(self, form):
        post_id = self.kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_id, status=1)
        form.instance.author = self.request.user
        form.instance.post = post
        return super().form_valid(form)
    
    def get_success_url(self):
        post = self.object.post
        return reverse('post_detail', kwargs={'pk': post.pk})

class UpdateCommentView(UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('blog.html')

    def get_object(self, queryset=None):
        comment_pk = self.kwargs.get('comment_pk')
        return get_object_or_404(Comment, pk=comment_pk)



class DeleteCommentView(DeleteView):
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('blog.html')


# def comment(request, pk):
#     post = get_object_or_404(Post, pk=pk, status=1)
#     comments = post.comments.all().order_by("-created_on")
#     comment = None
#     print('one')

#     if request.method == 'POST':
#         print('2')
#         comment_form = CommentForm(data=request.POST)
#         if comment_form.is_valid():
#             print('3')
#             comment = comment_form.save(commit=False)
#             print('4')
#             comment.author = request.user
#             comment.post = post
#             print(comment.author)
#             comment.save()
#         return render(request, 'blog.html')
#     else:
#         comment_form = CommentForm()

#     return render(request, 'add_comment.html', {
#         'post': post,
#         'comments': comments,
#         'comment': comment,
#         'comment_form': comment_form,
#     })
    




