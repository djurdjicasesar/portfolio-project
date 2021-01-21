from django.shortcuts import render
from django.views.generic import ListView
from .models import Blog

def allposts(request):
    blogs = Blog.objects
    return render(request, 'blog/allposts.html', {'blogs': blogs})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/allposts.html'
    context_object_name = 'blogs'
    ordering = ['-pub_date']
