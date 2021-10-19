import graphene
from graphene_django import DjangoObjectType

from todoapp.models import ToDo, Project
from userapp.models import ToDoUser


class UserType(DjangoObjectType):
    class Meta:
        model = ToDoUser
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)
    all_projects = graphene.List(ProjectType)
    all_notices = graphene.List(ToDoType)
    user_by_id = graphene.Field(UserType, id=graphene.Int(required=True))
    notices_by_username = graphene.List(
        ToDoType, name=graphene.String(
            required=False))

    def resolve_all_users(self, info):
        return ToDoUser.objects.all()

    def resolve_all_projects(self, info):
        return Project.objects.all()

    def resolve_all_notices(self, info):
        return ToDo.objects.all()

    def resolve_user_by_id(self, info, id):
        try:
            return ToDoUser.objects.get(pk=id)
        except ToDoUser.DoesNotExist:
            return None

    def resolve_notices_by_username(self, info, name=None):
        notices = ToDo.objects.all()
        if name:
            notices = notices.filter(user__username=name)
        return notices


schema = graphene.Schema(query=Query)
