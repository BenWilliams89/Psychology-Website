from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("accounts/", include("allauth.urls")),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog-urls'),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
]
