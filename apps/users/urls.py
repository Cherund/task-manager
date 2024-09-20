from django.urls import path

from apps.users.views import UserIndexView, UserCreateView, UserUpdateView, UserDeleteView

urlpatterns = [
    path('', UserIndexView.as_view(), name='users'),
    path('create/', UserCreateView.as_view(), name='users_create'),
    path('<int:pk>/update/', UserUpdateView.as_view(), name='users_update'),
    path('<int:pk>/delete/', UserDeleteView.as_view(), name='users_delete'),

]
