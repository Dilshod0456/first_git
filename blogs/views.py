from typing import Any
from .models import Blog
from .forms import BlogForm
from django.db.models import Q
from django.urls import reverse_lazy
from django.shortcuts import (
    render, 
    redirect, 
    get_object_or_404,
    )
from django.views.generic import (
    ListView, 
    CreateView, 
    DetailView, 
    UpdateView, 
    DeleteView, 
    TemplateView,
    )
from django.db.models import Count
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='login')
def blogLikeView(request, pk):
    blog = get_object_or_404(Blog, id = pk)
    if request.user in blog.likes.all():
        blog.likes.remove(request.user)
    else:
        blog.likes.add(request.user)

    # old_page = request.META["HTTP_REFERER"]
    # if '?next=' in old_page:
    #     # Agar next parametri yo'q bo'lsa, standart sahifaga qaytish
    #     return redirect('blogs:blog_home')
    return redirect((request.META["HTTP_REFERER"]))

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

        yangiliklar = yangiliklar.annotate(likes_count=Count('likes'))
        return yangiliklar
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['context'] = "qo'shimcha ma'lumotlar uchun"
        return context

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