from django.urls import path
from .views import *

app_name = "app1"

urlpatterns = [
    path('', IndexView.as_view(), name="home"),
]