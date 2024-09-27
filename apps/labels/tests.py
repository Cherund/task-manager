from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from apps.core.mixins import SetUpLoggedUserMixin
from apps.labels.forms import LabelForm
from apps.labels.models import Label
from apps.statuses.models import Status
from apps.tasks.models import Task
from django.utils.translation import gettext as _


class LabelIndexViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.label = Label.objects.create(name='Test Label')

    def test_label_list_view_status_code(self):
        response = self.client.get(reverse('labels'))
        self.assertEqual(response.status_code, 200)

    def test_label_list_view_template(self):
        response = self.client.get(reverse('labels'))
        self.assertTemplateUsed(response, 'apps/labels/labels.html')

    def test_label_list_view_context(self):
        response = self.client.get(reverse('labels'))
        self.assertIn('labels', response.context)
        self.assertEqual(len(response.context['labels']), 1)
        self.assertEqual(response.context['labels'][0].name, 'Test Label')


class LabelCreateViewTest(SetUpLoggedUserMixin, TestCase):

    def test_create_label_view_status_code(self):
        response = self.client.get(reverse('labels_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_label_form(self):
        response = self.client.get(reverse('labels_create'))
        self.assertIsInstance(response.context['form'], LabelForm)

    def test_create_label_success(self):
        data = {'name': 'New Label'}
        response = self.client.post(reverse('labels_create'), data)
        self.assertRedirects(response, reverse('labels'))
        self.assertTrue(Label.objects.filter(name='New Label').exists())


class LabelUpdateViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.label = Label.objects.create(name='Test Label')

    def test_update_label_view_status_code(self):
        response = self.client.get(reverse('labels_update',
                                           kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)

    def test_update_label_success(self):
        data = {'name': 'Updated Label'}
        response = self.client.post(reverse('labels_update',
                                            kwargs={'pk': self.label.pk}),
                                    data)
        self.assertRedirects(response, reverse('labels'))
        self.label.refresh_from_db()
        self.assertEqual(self.label.name, 'Updated Label')


class LabelDeleteViewTest(SetUpLoggedUserMixin, TestCase):

    def setUp(self):
        super().setUp()
        self.label = Label.objects.create(name='Test Label')

    def test_delete_label_view_status_code(self):
        response = self.client.get(reverse('labels_delete',
                                           kwargs={'pk': self.label.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_label_success(self):
        response = self.client.post(reverse('labels_delete',
                                            kwargs={'pk': self.label.pk}))
        self.assertRedirects(response, reverse('labels'))
        self.assertFalse(Label.objects.filter(name='Test Label').exists())

    def test_delete_label_with_tasks(self):
        self.status = Status.objects.create(name='Test Status')

        self.task = Task.objects.create(name='Test Task', status=self.status,
                                        creator=self.user, executor=self.user,)

        self.task.labels.add(self.label)

        response = self.client.post(reverse('labels_delete',
                                            kwargs={'pk': self.label.pk}))
        self.assertRedirects(response, reverse('labels'))
        self.assertTrue(Label.objects.filter(pk=self.label.pk).exists())

        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]),
                         _('Unable to delete a label because it is being used'))
