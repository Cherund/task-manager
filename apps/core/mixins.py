from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request,
                       _('You are not logged in! Please log in.'))
        return redirect(reverse('login'))


class SetUpLoggedUserMixin:
    @classmethod
    def setUpTestData(cls):
        cls.logged_user_data = {'username': 'testuser',
                                'password': 'xsw23edc'}
        cls.logged_user = get_user_model().objects.create_user(
            username=cls.logged_user_data['username'],
            password=cls.logged_user_data['password']
        )

    def setUp(self):
        self.client.login(username=self.logged_user.username,
                          password=self.logged_user_data['password'])
