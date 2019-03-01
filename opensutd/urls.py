from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('projects.urls')),
    path('secretadmin/', admin.site.urls),
]
