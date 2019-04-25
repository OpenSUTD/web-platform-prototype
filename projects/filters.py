import django_filters
from .models import Project

class ProjectFilter(django_filters.FilterSet):

    CATEGORY_CHOICES = (
        ("UROP", "UROP Projects"),
        ("UTOP", "UTOP Projects"),
        ("ACAD", "Academic Projects"),
        ("SELF", "Self-Initiated Projects"),
        ("NONE", "Other Projects")
    )

    title = django_filters.CharFilter(max_length=200, lookup_expr='icontains', label='Project Title')
    category = django_filters.ChoiceFilter(choices=CATEGORY_CHOICES, label='Category')
    tags__name = django_filters.CharFilter(max_length=50, lookup_expr='iexact', label='Tag')

    class Meta:
        model = Project
        fields = ['title', 'category', 'tags__name']