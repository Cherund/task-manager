"""task_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from apps.core.views import IndexView
from apps.users.views import UserLoginView, UserLogoutView
from django.conf.urls.i18n import set_language


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('users/', include('apps.users.urls')),
    path('statuses/', include('apps.statuses.urls')),
    path('labels/', include('apps.labels.urls')),
    path('tasks/', include('apps.tasks.urls')),
    path('admin/', admin.site.urls, name='admin'),
    path('set_language/', set_language, name='set_language'),
]
