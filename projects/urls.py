from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index),
    path('users/<username>/', views.user_view, name="user"),
    path('projects/', views.projects_list_view, name="projects_list"),
    path('projects/<project_uid>/', views.project_view, name="showcase"),
    path('admin/approve', views.approval_view, name='approval')
]
