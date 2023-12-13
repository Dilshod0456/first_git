from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
from .forms import BlogForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.

class HomeView(ListView):
    template_name = 'blog/blog_list.html'
    model = Blog
    context_object_name = 'blogs'

    def get_queryset(self):
        if 'search' in self.request.GET:
            search = self.request.GET.get('search')
            yangiliklar = Blog.objects.filter(Q(Q(description__icontains = search)| Q(title__icontains = search)))
        else:
            yangiliklar = Blog.objects.all()
        return yangiliklar

class BDetailView(DetailView):
    template_name = 'blog/blog_details.html'
    model = Blog
    context_object_name = 'blog'
    
class BCreateView(CreateView):
    template_name = 'blog/create.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blog_home')

class BUpdateView(UpdateView):
    template_name = 'blog/create.html'
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blogs:blog_home')

class BDeleteView(DeleteView):
    model = Blog 
    success_url = reverse_lazy('blogs:blog_home')
    template_name = 'blog/delete.html'