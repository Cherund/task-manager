from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView


# def index(request):
#     return render(request, 'index.html')

class IndexView(TemplateView):
    template_name = 'index.html'


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
