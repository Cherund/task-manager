from django.urls import path
from apps.statuses import views


urlpatterns = [
    path('', views.StatusIndexView.as_view(), name='statuses'),
    path('create/', views.StatusCreateView.as_view(), name='statuses_create')
    ]