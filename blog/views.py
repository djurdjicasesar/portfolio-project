from django.shortcuts import render

from .models import Blog

def allposts(request):
    blogs = Blog.objects
    return render(request, 'blog/allposts.html', {'blogs': blogs})
