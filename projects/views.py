from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from . import models

# TODO: Dashboard, User Profile, Submit New Project
# TODO: HTML Pages for the above
# TODO: Fix the login page so that it authenticates

# Test that each page runs correctly
# Test that unapproved projects return 404 to user (but not to admins)
# Test that home page only displays approved projects

class LoginPageView(generic.ListView):
    template_name = 'projects/login.html'
    context_object_name = 'login'

    def get_queryset(self):
        return models.User.objects

class ProjectListView(generic.ListView):
    template_name = 'projects/list.html'
    context_object_name = 'projects_list'

    def get_queryset(self):
    # TODO: Filter by "Approved" Projects
        return models.Project.objects

def project_view(request, project_uid):
    current_project = models.Project.objects.get(project_uid=project_uid)
    print(current_project)
    context = {'current_project': current_project}
    return render(request, 'projects/showcase.html', context)

class ApprovalView(generic.ListView):
    template_name = 'projects/toapprove.html'
    context_object_name = 'to_approve'

    def get_queryset(self):
    # TODO: Filter by "Pending Projects
        return models.Project.objects