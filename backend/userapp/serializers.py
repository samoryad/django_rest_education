from rest_framework.serializers import ModelSerializer
from .models import ToDoUser


class UserModelSerializer(ModelSerializer):
    """сериализатор для пользователя ToDoUser"""
    class Meta:
        model = ToDoUser
        fields = '__all__'


class UserModelSerializerV1(ModelSerializer):
    """сериализатор для пользователя ToDoUser V1"""
    class Meta:
        model = ToDoUser
        fields = ('username', 'first_name', 'last_name', 'email')


class UserModelSerializerV2(ModelSerializer):
    """сериализатор для пользователя ToDoUser V2"""
    class Meta:
        model = ToDoUser
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'is_superuser',
            'is_staff')
