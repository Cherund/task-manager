from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser, User


def get_full_name(self):
    return f'{self.first_name} {self.last_name}'


get_user_model().add_to_class('__str__', get_full_name)

# class User(models.Model):
#     name = models.CharField(max_length=200)
#     surname = models.CharField(max_length=200)
#     nickname = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f'{self.nickname} {self.surname}'
