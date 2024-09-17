from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from apps.users.forms import CustomUserCreationForm, CustomUserChangeForm
from django.conf import settings
from django.utils.translation import gettext as _
from django.contrib import messages


class UserIndexView(ListView):
    template_name = 'apps/users/users.html'
    model = get_user_model()
    context_object_name = 'users'


class UserCreateView(SuccessMessageMixin, CreateView):
    template_name = 'apps/users/create.html'
    form_class = CustomUserCreationForm
    success_url = settings.LOGIN_URL
    success_message = _('The user has been successfully registered')


class UserUpdateView(SuccessMessageMixin, UserPassesTestMixin, UpdateView):
    model = get_user_model()
    form_class = CustomUserChangeForm
    template_name = 'apps/users/update.html'
    success_url = reverse_lazy('users')
    success_message = _('The user has been successfully updated')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized to modify another user.'))
        return redirect('users')


class UserDeleteView(SuccessMessageMixin, UserPassesTestMixin, DeleteView):
    model = get_user_model()
    template_name = 'apps/users/delete.html'
    success_url = reverse_lazy('users')
    success_message = _('The user has been successfully deleted')

    def test_func(self):
        user = self.get_object()
        return self.request.user == user

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized to modify another user.'))
        return redirect('users')
