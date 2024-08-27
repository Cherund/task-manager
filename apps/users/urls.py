from django.urls import path
from apps.users import views


urlpatterns = [
    # path('', views.users),
    path('create/', views.UserCreateView.as_view(), name='users_create'),
    # path('<int:pk>/update/', views.update),
    # path('<int:pk>/delete/', views.delete),
]
