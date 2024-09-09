from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.statuses.forms import StatusForm
from apps.statuses.models import Status
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib import messages


# Create your views here.
class StatusIndexView(LoginRequiredMixin, ListView):
    template_name = 'apps/statuses/statuses.html'
    model = Status
    context_object_name = 'statuses'

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'apps/statuses/create.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully created')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'apps/statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'apps/statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully deleted.')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')
