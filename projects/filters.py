import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):

    title = django_filters.CharFilter(max_length=200, lookup_expr='icontains', label='Project Title')
    project_uid = django_filters.CharFilter(max_length=20, lookup_expr='icontains', label='Project UID')
    tags__name = django_filters.CharFilter(max_length=50, lookup_expr='iexact', label='Tag')

    class Meta:
        model = Project
        fields = ['title', 'project_uid']