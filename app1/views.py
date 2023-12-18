from django.shortcuts import render, redirect
from django.views.generic import *
from django.contrib.auth import authenticate, login as auth_login
from .forms import UserForm
from django.contrib.auth.views import LogoutView
from django.contrib import messages

# Create your views here.
class IndexView(TemplateView):
    template_name = "home.html"

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            auth_login(request, user)
            messages.success(request, "Muvofaqqiyatli tizimga kirdingiz.")
        else:
            messages.error(request, "Tizimga kirolmadingiz.")

        try:
            return redirect(request.GET['next'])
        except:
            return redirect('/')      
    return render(request, 'registration/login.html', context={'form':UserForm})        


class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
