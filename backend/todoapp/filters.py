from django_filters import rest_framework as filters
from todoapp.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['name']


class ToDoFilter(filters.FilterSet):
    project = filters.ModelChoiceFilter(queryset=Project.objects.all())
    created = filters.DateFromToRangeFilter(label='Choose dates from to')

    class Meta:
        model = ToDo
        fields = ['project']
