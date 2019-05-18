from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import *
from django.utils import timezone

def index(request):
    posts = Post.objects.all()
    return render(request, "crudApp/index.html", {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'crudApp/detail.html', {'post': post})
'''
def create(request):
    if request.method == "GET":
        return render(request, "crudApp/create.html")
    else:
        form = PostForm(request.POST)
        form.save()
        posts = Post.objects.all()
        return render(request, "crudApp/index.html", {'posts': posts})
'''
def create(request):
    if request.method == "GET":
        return render(request, "crudApp/create.html")
    else:
        post = Post()
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('index')

def update(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        return render(request, "crudApp/update.html", {'post':post})
    else:
        post.title = request.POST['title']
        post.content = request.POST['content']
        post.pub_date = timezone.datetime.now()
        post.save()
        return redirect('index')

def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        return render(request, "crudApp/delete.html", {'post':post})
    else:
        post.delete()
        return redirect('index')