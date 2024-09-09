from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from apps.tasks.forms import TaskForm
from django.utils.translation import gettext as _
from apps.tasks.models import Task


class TaskIndexView(LoginRequiredMixin, ListView):
    template_name = 'apps/tasks/tasks.html'
    model = Task
    context_object_name = 'tasks'

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


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

