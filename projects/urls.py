from django.urls import path

from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='home'),
    path('students/', views.students_page_view, name="students"),
    path('educators/', views.educators_page_view, name="educators"),
    path('leaders/', views.leaders_page_view, name="leaders"),
    path('users/<user_id>/', views.user_view, name="user"),
    path('users/edit/<user_id>/', views.user_edit_view.as_view(), name="user_edit"),
    path('projects/', views.project_list_view, name="projects_list"),
    path('projects/<project_uid>/', views.project_view, name="project_page"),
    path('projects/bypass/<project_uid>/', views.project_view_bypass, name="project_page_bypass"),
    path('admin/approval', views.approval_view, name='approval'),
    path('admin/submit', views.submit_new_project, name='submit_new'),
    path('actions/reject/<project_uid>/', views.reject, name='reject'),
    path('actions/approve/<project_uid>/', views.approve, name='approve'),
]

handler404 = 'projects.views.custom_404'
