from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.translation import gettext as _

from apps.labels.models import Label
from apps.statuses.models import Status
from apps.tasks.models import Task


class CustomLoginRequiredMixin(LoginRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request,
                       _('You are not logged in! Please log in.'))
        return redirect(reverse('login'))


class SetUpLoggedUserMixin:
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username': 'testuser',
                         'password': 'xsw23edc'}
        cls.user = get_user_model().objects.create_user(
            username=cls.user_data['username'],
            password=cls.user_data['password']
        )

    def setUp(self):
        self.client.login(username=self.user.username,
                          password=self.user_data['password'])


class SetUpLoggedUserWithLabelMixin(SetUpLoggedUserMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.label = Label.objects.create(name='Test Label')


class SetUpLoggedUserWithStatusMixin(SetUpLoggedUserMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.status = Status.objects.create(name='Test Status')


class SetUpLoggedUserWithTaskMixin(SetUpLoggedUserMixin):
    @classmethod
    def setUpTestData(cls):
        super().setUpTestData()
        cls.status = Status.objects.create(name='Test Status')
        cls.task = Task.objects.create(name='Test Task',
                                       status=cls.status,
                                       creator=cls.user)
