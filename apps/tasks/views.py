from django.views.generic import TemplateView


class TaskIndexView(TemplateView):
    template_name = 'apps/tasks/tasks.html'
