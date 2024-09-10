from django.contrib.auth import get_user_model
from django_filters import rest_framework as filters
from apps.labels.models import Label
from apps.statuses.models import Status
from apps.tasks.models import Task


class TaskFilter(filters.FilterSet):
    status = filters.ModelChoiceFilter(queryset=Status.objects.all(), label='Статус')
    executor = filters.ModelChoiceFilter(queryset=get_user_model().objects.all(), label='Исполнитель')
    labels = filters.ModelMultipleChoiceFilter(queryset=Label.objects.all(), label='Метки')

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
