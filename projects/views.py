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

class HomepageView(generic.ListView):
    template_name = 'projects/home.html'
    context_object_name = 'homepage'

    def get_queryset(self):
    # TODO: Filter by "Approved" Projects
        return models.Project.objects

class ProjectView(generic.ListView):
    template_name = 'projects/project.html'
    context_object_name = 'project'
    def get_queryset(self):
        # TODO: Replace with specific project object (or use DetailView)
        return models.Project.objects

class ApprovalView(generic.ListView):
    template_name = 'projects/toapprove.html'
    context_object_name = 'to_approve'

    def get_queryset(self):
    # TODO: Filter by "Pending Projects
        return models.Project.objects