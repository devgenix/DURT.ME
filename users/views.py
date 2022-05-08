from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def home(request):
    if User:
        return render(request, 'unauth/home.html')
    else:
        return render(request, 'users/home.html')