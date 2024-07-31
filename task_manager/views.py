from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def statuses(request):
    return render(request, 'statuses.html')


def labels(request):
    return render(request, 'labels.html')


def tasks(request):
    return render(request, 'tasks.html')
