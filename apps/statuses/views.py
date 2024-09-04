from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.statuses.forms import StatusForm
from apps.statuses.models import Status
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


# Create your views here.
class StatusIndexView(ListView):
    template_name = 'apps/statuses/statuses.html'
    model = Status
    context_object_name = 'statuses'


class StatusCreateView(SuccessMessageMixin, CreateView):
    template_name = 'apps/statuses/create.html'
    form_class = StatusForm
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully created')


class StatusUpdateView(SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'apps/statuses/update.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully updated')


class StatusDeleteView(DeleteView):
    model = Status
    template_name = 'apps/statuses/delete.html'
    success_url = reverse_lazy('statuses')
    success_message = _('The status has been successfully deleted.')
