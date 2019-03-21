from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.decorators import login_required

from . import models

# TODO: Dashboard, User Profile, Submit New Project

# Test that each page runs correctly


def index(request):
    top_projects_list = models.Project.objects.order_by('-published_date')[:2]
    recent_projects_list = models.Project.objects.order_by(
        '-published_date')[:9]
    context = {'top_projects_list': top_projects_list,
               'recent_projects_list': recent_projects_list}
    return render(request, 'opensutd/home.html', context)


def user_view(request, user_id):
    current_user = models.User.objects.get(username=user_id)
    context = {'current_user': current_user}
    return render(request, 'opensutd/user.html', context)


def project_view(request, project_uid):
    current_project = models.Project.objects.get(project_uid=project_uid)
    context = {'current_project': current_project}
    return render(request, 'projects/showcase.html', context)


def projects_list_view(request):
    projects_list = models.Project.objects.order_by('-published_date')[:50]
    context = {'projects_list': projects_list}
    return render(request, 'projects/list.html', context)


@login_required
def approval_view(request):
    context = {}
    return render(request, 'opensutd/admin_pending.html', context)
