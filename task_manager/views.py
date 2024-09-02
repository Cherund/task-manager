from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from task_manager.settings import LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = LOGIN_REDIRECT_URL
    success_message = _('You have successfully logged in')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = LOGOUT_REDIRECT_URL
    success_message = _('You have successfully logged out')


def statuses(request):
    return render(request, 'statuses.html')


def labels(request):
    return render(request, 'labels.html')


def tasks(request):
    return render(request, 'tasks.html')
