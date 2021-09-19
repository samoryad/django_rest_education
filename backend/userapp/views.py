from rest_framework.viewsets import ModelViewSet
from .models import ToDoUser
from .serializers import UserModelSerializer


class ToDoUserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = ToDoUser.objects.all()
