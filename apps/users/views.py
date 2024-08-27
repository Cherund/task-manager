from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView
from apps.users.forms import CustomUserCreationForm


#
#
# def users(request):
#     return render(request, 'users.html')
#
#
# # def register(request):
# #     return render(request, 'create.html')
#


class UserCreateView(CreateView):
    template_name = 'create.html'
    form_class = CustomUserCreationForm

#
# def update(request):
#     return None
#
#
# def delete(request):
#     return None
