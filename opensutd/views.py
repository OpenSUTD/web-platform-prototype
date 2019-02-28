from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from projects import models

def index(request):
    # pick top 5 recent projects
    latest_projects_list = models.Project.objects.order_by('-published_date')[:5]
    print(latest_projects_list)
    context = {'latest_projects_list': latest_projects_list}
    return render(request, 'opensutd/home.html', context)