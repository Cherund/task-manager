from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from apps.labels.models import Label
from apps.statuses.models import Status
from apps.tasks.filters import TaskFilter
from apps.tasks.forms import TaskForm
from django.utils.translation import gettext as _
from apps.tasks.models import Task
from django_filters.views import FilterView


class TaskIndexView(LoginRequiredMixin, FilterView, ListView):
    template_name = 'apps/tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'
    filter_class = TaskFilter

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Получение уникальных меток для всех задач
        context['unique_statuses'] = Status.objects.filter(tasks__in=self.get_queryset()).distinct()
        context['unique_executors'] = get_user_model().objects.filter(executor_tasks__in=self.get_queryset()).distinct()
        context['unique_labels'] = Label.objects.filter(tasks__in=self.get_queryset()).distinct()
        return context


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'apps/tasks/create.html'
    form_class = TaskForm
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully registered')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'apps/tasks/update.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'apps/tasks/delete.html'
    success_url = reverse_lazy('tasks')
    success_message = _('The task has been successfully deleted.')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class TaskSingleView(DetailView):
    model = Task
    template_name = 'apps/tasks/task.html'
    context_object_name = 'task'

