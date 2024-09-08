from django.urls import path
from apps.tasks import views


urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks'),
]
