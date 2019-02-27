from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('login', views.LoginPageView.as_view(), name='login'),
    path('list', views.ProjectListView.as_view(), name='projects_list'),
    path('project', views.ProjectView.as_view(), name='project'),
    path('approval', views.ApprovalView.as_view(), name='approval')
]

# TODO: Set project URL to match ID and display data from database