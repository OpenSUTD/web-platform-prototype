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

def index(request):
    top_projects_list = models.Project.objects.order_by('-published_date')[:2]
    recent_projects_list = models.Project.objects.order_by('-published_date')[:9]
    context = {'top_projects_list': top_projects_list,
               'recent_projects_list': recent_projects_list}
    return render(request, 'opensutd/home.html', context)

def project_view(request, project_uid):
    current_project = models.Project.objects.get(project_uid=project_uid)
    print(current_project)
    context = {'current_project': current_project}
    return render(request, 'projects/showcase.html', context)

def projects_list_view(request):
    projects_list = models.Project.objects.order_by('-published_date')[:50]
    context = {'projects_list': projects_list}
    return render(request, 'projects/list.html', context)

def login_view(request):
    context = {}
    return render(request, 'opensutd/login.html', context)

class ApprovalView(generic.ListView):
    template_name = 'projects/toapprove.html'
    context_object_name = 'to_approve'

    def get_queryset(self):
    # TODO: Filter by "Pending Projects
        return models.Project.objects
