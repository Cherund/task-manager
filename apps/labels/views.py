from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from apps.labels.forms import LabelForm
from apps.labels.models import Label
from django.utils.translation import gettext as _
from django.urls import reverse_lazy


# Create your views here.
class LabelIndexView(ListView):
    template_name = 'apps/labels/labels.html'
    model = Label
    context_object_name = 'labels'


class LabelCreateView(SuccessMessageMixin, CreateView):
    template_name = 'apps/labels/create.html'
    form_class = LabelForm
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully created')


class LabelUpdateView(SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'apps/labels/update.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully updated')


class LabelDeleteView(DeleteView):
    model = Label
    template_name = 'apps/labels/delete.html'
    success_url = reverse_lazy('labels')
    success_message = _('The label has been successfully deleted.')
