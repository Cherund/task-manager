from django.urls import path
from apps.tasks import views

urlpatterns = [
    path('', views.TaskIndexView.as_view(), name='tasks'),
    path('create/', views.TaskCreateView.as_view(), name='tasks_create'),
    path('<int:pk>/update/', views.TaskUpdateView.as_view(), name='tasks_update'),
    path('<int:pk>/delete/', views.TaskDeleteView.as_view(), name='tasks_delete'),
    path('<int:pk>/', views.TaskSingleView.as_view(), name='tasks_single'),

]
