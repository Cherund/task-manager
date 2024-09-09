from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.labels.forms import LabelForm
from apps.labels.models import Label
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.
class LabelIndexView(LoginRequiredMixin, ListView):
    template_name = 'apps/labels/labels.html'
    model = Label
    context_object_name = 'labels'

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'apps/labels/create.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully created')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'apps/labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully updated')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'apps/labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully deleted.')

    def handle_no_permission(self):
        messages.error(self.request, _('You are not authorized. Please, log in'))
        return redirect('login')
