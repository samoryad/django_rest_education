from rest_framework.relations import StringRelatedField, SlugRelatedField, \
    PrimaryKeyRelatedField, HyperlinkedRelatedField
from rest_framework.serializers import ModelSerializer

from userapp.models import ToDoUser
from userapp.serializers import UserModelSerializer
from .models import ToDo, Project


class ProjectSerializer(ModelSerializer):
    """сериализатор для проектов"""
    # users = UserModelSerializer(many=True, read_only=True)
    # users = StringRelatedField(many=True)
    # users = HyperlinkedRelatedField(
    #     many=True,
    #     queryset=ToDoUser.objects.all(),
    #     view_name='todouser-detail')

    users = SlugRelatedField(
        many=True,
        slug_field='username',
        queryset=ToDoUser.objects.all())

    class Meta:
        model = Project
        fields = ['id', 'name', 'link', 'users']


class ToDoSerializer(ModelSerializer):
    """сериализатор для заметок"""
    project = SlugRelatedField(queryset=Project.objects.all(),
                               slug_field='name')
    # user = PrimaryKeyRelatedField(queryset=ToDoUser.objects.all())

    class Meta:
        model = ToDo
        fields = [
            'id',
            'project',
            'text',
            'created_date',
            'updated_date',
            'user',
            'is_active']
