from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User

def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(posts, 6)
    
    try:
        selectedPost = paginator.page(page)
    except PageNotAnInteger:
        selectedPost = paginator.page(1)
    except EmptyPage:
        selectedPost = paginator.page(paginator.num_pages)

    return render(request, "crudApp/index.html", {'posts': selectedPost})

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.all().filter(post=post)
    page = request.GET.get('page', 1)
    paginator = Paginator(comments, 5)

    try:
        selectedComments = paginator.page(page)
    except PageNotAnInteger:
        selectedComments = paginator.page(1)
    except EmptyPage:
        selectedComments = paginator.page(paginator.num_pages)
        
    return render(request, 'crudApp/detail.html', {'post': post, 'selectedComments':selectedComments})

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


def addComment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment = Comment()
    comment.post = post
    comment.content = request.POST['content']
    comment.save()
    return redirect('/' + str(post_id) + '/detail')