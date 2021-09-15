from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
