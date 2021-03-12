from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Blog



def allposts(request):
    blogs = Blog.objects
    return render(request, 'blog/allposts.html', {'blogs': blogs})

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/allposts.html'
    context_object_name = 'blogs'
    ordering = ['-pub_date']
    paginate_by = 2

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    fields = ['title', 'body', 'image']

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ['title', 'body', 'image']

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Blog
    success_url = '/blog/'

    
    
