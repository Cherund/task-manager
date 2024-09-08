from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.translation import gettext as _
from django.conf import settings
from django.contrib import messages


class IndexView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = settings.LOGIN_REDIRECT_URL
    success_message = _('You have successfully logged in')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    next_page = settings.LOGOUT_REDIRECT_URL

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out'))
        return super().dispatch(request, *args, **kwargs)
