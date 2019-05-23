from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password1']
            )
            return redirect('index')

def signin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password1']
        )

        if user is not None:
            auth.login(request, user)
            return reverse('index')
        else:
            return reverse('index')

def signout(request):
    if request.method == 'POST':
        auth.logout(request)
        return reverse('index')