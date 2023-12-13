from django.urls import path
from .views import *

app_name = "blogs"

urlpatterns = [
    path('', HomeView.as_view(), name="blog_home"),
    path('detail/<int:pk>', BDetailView.as_view(), name="blog_detail"),
    path('create/', BCreateView.as_view(), name="blog_create"),
    path('update/<int:pk>', BUpdateView.as_view(), name="blog_update"),
    path('delete/<int:pk>', BDeleteView.as_view(), name="blog_delete"),
]

