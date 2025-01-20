from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home.html'),
    path('blog/', views.PostList.as_view(), name='blog.html'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
