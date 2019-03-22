from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index),
    path('users/<user_id>/', views.user_view, name="user"),
    path('login', views.login_view, name="login"),
    path('projects/', views.projects_list_view, name="projects_list"),
    path('projects/<project_uid>/', views.project_view, name="showcase"),
    path('approval', views.ApprovalView.as_view(), name='approval'),

    path('registration/', views.UserRegistrationView.as_view(), name='register')
]
