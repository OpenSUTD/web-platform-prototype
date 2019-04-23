from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='home'),
    path('users/<user_id>/', views.user_view, name="user"),
    path('projects/', views.projects_list_view, name="projects_list"),
    path('projects/search', views.project_listfilter, name="projects_list_filter"),
    path('projects/<project_uid>/', views.project_view, name="project_page"),
    path('admin/approval', views.approval_view, name='approval'),
    path('admin/submit', views.submit_new_project, name='submit_new'),
    path('actions/reject/<project_uid>/', views.reject, name='reject'),
    path('actions/approve/<project_uid>/', views.approve, name='approve'),
]
