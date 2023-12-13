from django.forms import *
from .models import Blog

class BlogForm(ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'author',
            'image',
        ]