from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='home'),
    path('users/<user_id>/', views.user_view, name="user"),
    path('projects/', views.projects_list_view, name="projects_list"),
    path('projects/<project_uid>/', views.project_view, name="showcase"),
    path('admin/approval', views.approval_view, name='approval'),
    path('actions/reject/<project_uid>/', views.reject, name='reject'),
    path('actions/approve/<project_uid>/', views.approve, name='approve'),
    path('registration/', views.UserRegistrationView.as_view(), name='register')
]
