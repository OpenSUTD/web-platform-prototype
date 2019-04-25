import markdown2
import base64
from django.shortcuts import render
from django.views import generic

from django.views.generic import FormView
from django.http import *
from .forms import *
from .filters import ProjectFilter

from django.contrib.auth.decorators import login_required

from . import models

from github import Github

import os

ACCESS_TOKEN = os.environ["GH_ACCESS_TOKEN"]
gh = Github(ACCESS_TOKEN)


def index(request):
    top_projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="ACCEPT")[:4]
    recent_projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="ACCEPT")[:9]
    context = {"top_projects_list": top_projects_list,
               "recent_projects_list": recent_projects_list}
    return render(request, "opensutd/home.html", context)


def students_page_view(request):
    student_projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="ACCEPT").filter(tags__name__in=["student"])[:9]
    
    context = {"student_projects_list": student_projects_list}
    return render(request, "opensutd/students.html", context)


def educators_page_view(request):
    educators_projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="ACCEPT").filter(tags__name__in=["education"])[:9]
    
    context = {"educators_projects_list": educators_projects_list}
    return render(request, "opensutd/educators.html", context)


def leaders_page_view(request):
    policy_projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="ACCEPT").filter(tags__name__in=["policy"])[:9]
    
    context = {"policy_projects_list": policy_projects_list}
    return render(request, "opensutd/leaders.html", context)


def user_view(request, user_id):
    current_user = models.User.objects.get(username=user_id)
    user_projects = models.Project.objects.filter(users=current_user)
    context = {"current_user": current_user,
               "user_projects": user_projects}
    return render(request, "opensutd/user.html", context)


def get_readme(current_project_url):
    repo_url = current_project_url.split("/")
    repo_name = repo_url[-2] + "/" + repo_url[-1]
    repo = gh.get_repo(repo_name)
    readme = str(base64.b64decode(
        repo.get_contents("README.md").content))
    readme = readme.replace("\\n", "\n")
    readme = readme[2:-1]  # get rid of b' and '
    readme = markdown2.markdown(readme, extras=["fenced-code-blocks"])

    # fix image paths
    # ignore fully defined paths with http
    readme = readme.replace('src="http', '<|SPECIAL_TOKEN|>')
    readme = readme.replace(
        'src="', 'src="https://raw.githubusercontent.com/' + repo_name + '/master/')
    readme = readme.replace('<|SPECIAL_TOKEN|>', 'src="http')

    return readme


def project_view(request, project_uid):
    current_project = models.Project.objects.get(project_uid=project_uid)
    if current_project.is_accepted():
        try:
            readme = get_readme(current_project.url)
        except Exception as e:
            readme = "Unable to retrieve README:\n"+str(e)

        context = {"current_project": current_project,
                   "readme": readme}
        return render(request, "projects/showcase.html", context)
    else:
        # TODO: replace with OpenSUTD 404 page
        return HttpResponseNotFound("Project not approved!")


def project_list_view(request):
    f = ProjectFilter(
        request.GET, queryset=models.Project.objects.order_by("-published_date").filter(status="ACCEPT"))
    return render(request, "projects/list.html", {"filter": f})


@login_required
def submit_new_project(request):
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = SubmissionForm(request.POST)
        # check whether it"s valid:
        print(form)
        print(form.is_valid())
        if form.is_valid():
            # process the data in form.cleaned_data as required

            data = form.cleaned_data
            pm = models.OpenSUTDProjectManager()

            print(data)

            project_uid = data["project_name"].upper().replace(" ", "_")

            pm.create_project(project_uid=project_uid,
                              title=data["project_name"],
                              caption=data["caption"],
                              category=data["category"],
                              url=data["github_url"],
                              featured_image=data["featured_image"])

            # redirect to a new URL:
            return HttpResponseRedirect("/admin/approval")

    # if a GET (or any other method) we"ll create a blank form
    else:
        form = SubmissionForm()

    return render(request, "opensutd/submit_new.html", {"form": form})


@login_required
def approval_view(request):
    projects_list = models.Project.objects.order_by(
        "-published_date").filter(status="PENDING")[:50]
    context = {"projects_list": projects_list}
    return render(request, "opensutd/admin_pending.html", context)


@login_required
def approve(request, project_uid):
    project = models.Project.objects.get(project_uid=project_uid)
    project.status = "ACCEPT"
    project.save()
    return HttpResponseRedirect("/admin/approval")


@login_required
def reject(request, project_uid):
    project = models.Project.objects.get(project_uid=project_uid)
    project.status = "REJECT"
    project.save()
    return HttpResponseRedirect("/admin/approval")
