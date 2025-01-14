from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog_page_view(request):
    return HttpResponse('This is the start of my blog page')