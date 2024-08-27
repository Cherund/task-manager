from django.shortcuts import render, get_object_or_404, redirect
from django.views import View


# def index(request):
#     return render(request, 'index.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


def users(request):
    return render(request, 'users.html')


def login(request):
    return render(request, 'login.html')


def logout(request):
    return None


def statuses(request):
    return render(request, 'statuses.html')


def labels(request):
    return render(request, 'labels.html')


def tasks(request):
    return render(request, 'tasks.html')
