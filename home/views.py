from django.shortcuts import render, redirect

# Create your views here.
from .form import *

def home(request):
    context = {'blogs' : BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    return render(request, 'login.html')

def blog_detail(request, slug):
    return render(request, 'blog_detail.html')

def add_blog(request):
    context = {'form' : BlogForm}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST)
            print(request.FILES)
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user

            if form.is_valid():
                content = form.cleaned_data['content']

            blog_obj = BlogModel.objects.create(
                user = user , title = title,
                content = content, image = image,
            )
            print(blog_obj)
            return redirect('/add-blog/')
    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)

def register_view(request):
    return render(request, 'register.html')