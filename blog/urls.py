from django.urls import path
from .views import blog_page_view

urlpatterns = [
    path('', blog_page_view)
]
