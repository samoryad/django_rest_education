from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import ProjectFilter
from .models import Project, ToDo
from .serializers import ProjectSerializer, ToDoSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ToDoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
    pagination_class = ProjectLimitOffsetPagination
    filterset_class = ProjectFilter

    # для себя оставил (без подключения django-filter) через параметры запроса
    # например, http://127.0.0.1:8000/api/project/?name=1
    # def get_queryset(self):
    #     project_name = self.request.query_params.get('name')
    #     if project_name:
    #         result = Project.objects.filter(name__contains=project_name)
    #         if result:
    #             return result
    #     return self.queryset


class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoSerializer
    queryset = ToDo.objects.all()
    pagination_class = ToDoLimitOffsetPagination
    filterset_fields = ['project']

    # переопределяем метод destroy (вместо удаления - не активно)
    def destroy(self, request, *args, **kwargs):
        todo_notice = self.get_object()
        todo_notice.is_active = False
        todo_notice.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
