from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
