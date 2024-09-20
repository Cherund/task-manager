from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from apps.users.forms import CustomUserCreationForm
from django.conf import settings
from django.utils.translation import gettext as _


class UserIndexViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser',
                                                         password='xsw23edc')

    def test_user_list_view_status_code(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)

    def test_user_list_view_template(self):
        response = self.client.get(reverse('users'))
        self.assertTemplateUsed(response, 'apps/users/users.html')

    def test_user_list_view_context(self):
        response = self.client.get(reverse('users'))
        self.assertIn('users', response.context)
        self.assertEqual(len(response.context['users']), 1)


class UserCreateViewTest(TestCase):

    def test_create_user_view_status_code(self):
        response = self.client.get(reverse('users_create'))
        self.assertEqual(response.status_code, 200)

    def test_create_user_form(self):
        response = self.client.get(reverse('users_create'))
        self.assertIsInstance(response.context['form'], CustomUserCreationForm)

    def test_create_user_success(self):
        data = {
            'username': 'newuser',
            'first_name': 'New',
            'last_name': 'User',
            'password1': 'xsw23edc',
            'password2': 'xsw23edc',
        }
        response = self.client.post(reverse('users_create'), data)
        self.assertRedirects(response, settings.LOGIN_URL)
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())


class UserUpdateViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser',
                                                         password='xsw23edc')
        self.client.login(username='testuser', password='xsw23edc')

    def test_update_user_view_status_code(self):
        response = self.client.get(reverse('users_update',
                                           kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)

    def test_update_user_success(self):
        data = {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User',
            'password1': 'xsw23edc',
            'password2': 'xsw23edc',
        }
        response = self.client.post(reverse('users_update',
                                            kwargs={'pk': self.user.pk}),
                                    data)
        self.assertRedirects(response, reverse('users'))
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')


class UserDeleteViewTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser',
                                                         first_name='test',
                                                         last_name='user',
                                                         password='xsw23edc')
        self.client.login(username='testuser', password='xsw23edc')

    def test_delete_user_view_status_code(self):
        response = self.client.get(reverse('users_delete',
                                           kwargs={'pk': self.user.pk}))
        self.assertEqual(response.status_code, 200)

    def test_delete_user_success(self):
        response = self.client.post(reverse('users_delete',
                                            kwargs={'pk': self.user.pk}))
        self.assertRedirects(response, reverse('users'))
        self.assertFalse(get_user_model().objects.filter(username='testuser').exists())


class UserUpdateViewPermissionsTest(TestCase):

    def setUp(self):
        self.owner = get_user_model().objects.create_user(username='owner',
                                                          password='password123')
        self.other_user = get_user_model().objects.create_user(username='otheruser',
                                                               password='password123')
        self.client.login(username='owner', password='password123')

    def test_cannot_update_another_user(self):
        data = {
            'username': 'updateduser',
            'first_name': 'Updated',
            'last_name': 'User'
        }
        response = self.client.post(reverse('users_delete',
                                            kwargs={'pk': self.other_user.pk}),
                                    data)
        self.assertRedirects(response, reverse('users'))
        self.other_user.refresh_from_db()
        self.assertNotEqual(self.other_user.username, 'updateduser')

    def test_cannot_access_update_view_of_another_user(self):
        response = self.client.get(reverse('users_update',
                                           kwargs={'pk': self.other_user.pk}))
        self.assertRedirects(response, reverse('users'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]),
                         _('You are not authorized to modify another user.'))


class UserDeleteViewPermissionsTest(TestCase):

    def setUp(self):
        self.owner = get_user_model().objects.create_user(username='owner',
                                                          password='password123')
        self.other_user = get_user_model().objects.create_user(username='otheruser',
                                                               password='password123')
        self.client.login(username='owner', password='password123')

    def test_cannot_delete_another_user(self):
        response = self.client.post(reverse('users_delete',
                                            kwargs={'pk': self.other_user.pk}))
        self.assertRedirects(response, reverse('users'))
        self.assertTrue(
            get_user_model().objects.filter(username='otheruser').exists())

    def test_cannot_access_delete_view_of_another_user(self):
        response = self.client.get(reverse('users_delete',
                                           kwargs={'pk': self.other_user.pk}))
        self.assertRedirects(response, reverse('users'))
        messages = list(response.wsgi_request._messages)
        self.assertEqual(str(messages[0]),
                         _('You are not authorized to modify another user.'))
