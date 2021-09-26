from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.mixins import UpdateModelMixin, ListModelMixin, \
    RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import ToDoUser
from .serializers import UserModelSerializer


# # viewset для отображения всех операций, GET, POST, UPDATE, DELETE
# class ToDoUserViewSet(ModelViewSet):
#     serializer_class = UserModelSerializer
#     queryset = ToDoUser.objects.all()


class ToDoUserViewSet(
        UpdateModelMixin,
        ListModelMixin,
        RetrieveModelMixin,
        GenericViewSet):
    """
    viewset только для просмотра списка и обновления каждого пользователя
    удалять и создавать нельзя
    """
    queryset = ToDoUser.objects.all()
    serializer_class = UserModelSerializer

    # позволяет создать для конкретного юзера дополнительный метод вывода
    # username, например http://127.0.0.1:8000/api/users/2/username/
    @action(detail=True, methods=['GET'])
    def username(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'name': user.username})

    # позволяет создать для конкретного юзера дополнительный метод вывода
    # user_email, например http://127.0.0.1:8000/api/users/2/user_email/
    @action(detail=True, methods=['GET'])
    def user_email(self, request, pk=None):
        user = get_object_or_404(ToDoUser, pk=pk)
        return Response({'email': user.email})
