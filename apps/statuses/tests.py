from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.core.mixins import SetUpLoggedUserMixin
from apps.statuses.forms import StatusForm
from apps.statuses.models import Status
from apps.tasks.models import Task
from django.utils.translation import gettext as _


class StatusIndexViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.status = Status.objects.create(name='Test Status')

    def test_status_list_view_status_code(self):
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

    def test_status_list_view_template(self):
        response = self.client.get(reverse('statuses'))
        self.assertTemplateUsed(response, 'apps/statuses/statuses.html')

    def test_status_list_view_context(self):
        response = self.client.get(reverse('statuses'))
        self.assertIn('statuses', response.context)
        self.assertEqual(len(response.context['statuses']), 1)
        self.assertEqual(response.context['statuses'][0].name, 'Test Status')


class StatusCreateViewTest(SetUpLoggedUserMixin, TestCase):

    def test_create_status_view_status_code(self):
        response = self.client.get(reverse('statuses_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_status_form(self):
        response = self.client.get(reverse('statuses_create'))
        self.assertIsInstance(response.context['form'], StatusForm)

    def test_create_status_success(self):
        data = {'name': 'New Status'}
        response = self.client.post(reverse('statuses_create'), data)
        self.assertRedirects(response, reverse('statuses'))
        self.assertTrue(Status.objects.filter(name='New Status').exists())


class StatusUpdateViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.status = Status.objects.create(name='Test Status')

    def test_update_status_view_status_code(self):
        response = self.client.get(reverse('statuses_update',
                                           kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 200)

    def test_update_status_success(self):
        data = {'name': 'Updated Status'}
        response = self.client.post(reverse('statuses_update',
                                            kwargs={'pk': self.status.pk}),
                                    data)
        self.assertRedirects(response, reverse('statuses'))
        self.status.refresh_from_db()
        self.assertEqual(self.status.name, 'Updated Status')


class StatusDeleteViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.status = Status.objects.create(name='Test Status')

    def test_delete_status_view_status_code(self):
        response = self.client.get(reverse('statuses_delete',
                                           kwargs={'pk': self.status.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_status_success(self):
        response = self.client.post(reverse('statuses_delete',
                                            kwargs={'pk': self.status.pk}))
        self.assertRedirects(response, reverse('statuses'))
        self.assertFalse(Status.objects.filter(name='Test Status').exists())

    def test_delete_status_with_tasks(self):

        self.task = Task.objects.create(name='Test Task', status=self.status,
                                        creator=self.user, executor=self.user)

        response = self.client.post(reverse('statuses_delete',
                                            kwargs={'pk': self.status.pk}))
        self.assertRedirects(response, reverse('statuses'))
        self.assertTrue(Status.objects.filter(pk=self.status.pk).exists())

        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]),
                         _('Unable to delete a status because it is being used'))
