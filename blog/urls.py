from django.urls import path
from . import views
from .views import post_detail, PostAdd, UpdatePostView, DeletePostView, CommentAdd, UpdateCommentView, DeleteCommentView

urlpatterns = [
    path('', views.home, name='home.html'),
    path('blog/', views.PostList.as_view(), name='blog.html'),
    path('post/<int:pk>/', post_detail('request', 'title','author','content', 'content'), name='post_detail'),
    path('add_blog/', PostAdd.as_view(), name='add_post'),
    path('post/edit<int:pk>/', UpdatePostView.as_view(), name='update_post'),
    path('post/<int:pk>delete/', DeletePostView.as_view(), name='delete_post'),
    path('comment/<int:pk>/', CommentAdd.as_view(), name='add_comment'),
    path('comment/edit<int:pk>/', UpdateCommentView.as_view(), name='update_comment'),
    path('comment/<int:pk>delete/', DeleteCommentView.as_view(), name='delete_comment'),
]
