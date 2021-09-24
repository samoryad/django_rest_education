from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer
from .models import ToDo, Project


class ProjectSerializer(ModelSerializer):
    """сериализатор для проектов"""
    users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = ['name', 'link', 'users']


class ToDoSerializer(ModelSerializer):
    """сериализатор для заметок"""

    class Meta:
        model = ToDo
        fields = [
            'project',
            'text',
            'created_date',
            'updated_date',
            'user',
            'is_active']
