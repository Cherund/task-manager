from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User


def get_full_name(self):
    return f'{self.first_name} {self.last_name}'


get_user_model().add_to_class('__str__', get_full_name)

