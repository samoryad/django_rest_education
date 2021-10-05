from rest_framework.permissions import IsAuthenticatedOrReadOnly, \
    BasePermission
from rest_framework.viewsets import ModelViewSet
from .models import Author
from .serializers import AuthorSerializer


# собственная проверка на права администратора
class CustomPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff


class AuthorViewSet(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
    # допуск только авторизованному пользователю или только чтение
    permission_classes = [IsAuthenticatedOrReadOnly]
