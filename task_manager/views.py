from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')
