from django.shortcuts import render

# Create your views here.
from .form import *

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')

def add_blog(request):
    context = {'form' : BlogForm}
    return render(request, 'add_blog.html', context)

def register_view(request):
    return render(request, 'register.html')