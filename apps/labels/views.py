from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.labels.forms import LabelForm
from apps.labels.models import Label
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from task_manager.mixins import CustomLoginRequiredMixin


# Create your views here.
class LabelIndexView(CustomLoginRequiredMixin, ListView):
    template_name = 'apps/labels/labels.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(CustomLoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'apps/labels/create.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully created')


class LabelUpdateView(CustomLoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'apps/labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully changed')


class LabelDeleteView(CustomLoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = 'apps/labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully deleted')
