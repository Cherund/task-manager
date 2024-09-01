from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from apps.users.forms import CustomUserCreationForm
from task_manager.settings import LOGIN_URL, LOGIN_REDIRECT_URL, LOGOUT_REDIRECT_URL
from django.utils.translation import gettext as _


#
#
class IndexView(ListView):
    template_name = 'apps/users/users.html'
    model = get_user_model()
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'apps/users/create.html'
    form_class = CustomUserCreationForm
    success_url = LOGIN_URL
    success_message = _('The user has been successfully registered')


class UserUpdateView(SuccessMessageMixin, UpdateView):
    template_name = 'apps/users/update.html'
    # form_class = CustomUserChangeForm
    form_class = CustomUserCreationForm
    model = get_user_model()
    success_url = reverse_lazy('users')
    success_message = _('The users has been successfully updated')


class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = get_user_model()
    template_name = 'apps/users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('The users has been successfully deleted')


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'apps/users/login.html'
    form_class = AuthenticationForm
    success_url = LOGIN_REDIRECT_URL
    success_message = _('You have successfully logged in')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = LOGOUT_REDIRECT_URL
    success_message = _('You have successfully logged out')
