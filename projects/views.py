from django.shortcuts import render
from django.views import generic

from django.views.generic import FormView
from django.http import *
from .forms import RegistrationForm
from .filters import ProjectFilter

from django.contrib.auth.decorators import login_required


from . import models

# TODO: Dashboard, User Profile, Submit New Project

# Test that each page runs correctly


def index(request):
    top_projects_list = models.Project.objects.order_by('-published_date')[:2]
    recent_projects_list = models.Project.objects.order_by(
        '-published_date').filter(status="ACCEPT")[:9]
    context = {'top_projects_list': top_projects_list,
               'recent_projects_list': recent_projects_list}
    return render(request, 'opensutd/home.html', context)


def user_view(request, user_id):
    current_user = models.User.objects.get(username=user_id)
    context = {'current_user': current_user}
    return render(request, 'opensutd/user.html', context)


def project_view(request, project_uid):
    current_project = models.Project.objects.get(project_uid=project_uid)
    if current_project.is_accepted():
        context = {'current_project': current_project}
        return render(request, 'projects/showcase.html', context)
    else:
        # TODO: replace with OpenSUTD 404 page
        return HttpResponseNotFound("Project not approved!")

def project_listfilter(request):
    f = ProjectFilter(request.GET, queryset=models.Project.objects.all().filter(status="ACCEPT"))
    return render(request, 'projects/listfilter.html', {'filter': f})

def projects_list_view(request):
    projects_list = models.Project.objects.order_by(
        '-published_date').filter(status="ACCEPT")[:50]
    context = {'projects_list': projects_list}
    return render(request, 'projects/list.html', context)


@login_required
def approval_view(request):
    projects_list = models.Project.objects.order_by(
        '-published_date').filter(status="PENDING")[:50]
    context = {'projects_list': projects_list}
    return render(request, 'opensutd/admin_pending.html', context)

@login_required
def approve(request, project_uid):
    project = models.Project.objects.get(project_uid=project_uid)
    project.status = "ACCEPT"
    project.save()
    return HttpResponseRedirect('/admin/approval')

@login_required
def reject(request, project_uid):
    project = models.Project.objects.get(project_uid=project_uid)
    project.status = "REJECT"
    project.save()
    return HttpResponseRedirect('/admin/approval')

class UserRegistrationView(FormView):
    form_class = RegistrationForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        models.UserRegister.objects.create_user(
            username=username, password=password)
        res_data = {
            'error': False,
            'message': 'Success, Please login'
        }
        return JsonResponse(res_data)

    def form_invalid(self, form):
        res_data = {
            'error': True,
            'errors': "error"
        }
        return JsonResponse(res_data)
