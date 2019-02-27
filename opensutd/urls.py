from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index),
    path('projects/', include('projects.urls')),
    path('admin/', admin.site.urls),
]
