from django.urls import path
from . import views
from .views import PostDetail, PostAdd, UpdatePostView

urlpatterns = [
    path('', views.home, name='home.html'),
    path('blog/', views.PostList.as_view(), name='blog.html'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('add_blog/', PostAdd.as_view(), name='add_post'),
    path('blog/edit<int:pk>/', UpdatePostView.as_view(), name='update_post'),
]
