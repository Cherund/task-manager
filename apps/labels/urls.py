from django.urls import path
from apps.labels import views


urlpatterns = [
    path('', views.LabelIndexView.as_view(), name='labels'),
    path('create/', views.LabelCreateView.as_view(), name='labels_create'),
    path('<int:pk>/update/', views.LabelUpdateView.as_view(), name='labels_update'),
    path('<int:pk>/delete/', views.LabelDeleteView.as_view(), name='labels_delete'),
]
