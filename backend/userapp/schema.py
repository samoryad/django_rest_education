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
    project_by_users = graphene.List(
        ProjectType, name=graphene.String(required=False)
    )

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

    def resolve_project_by_users(self, info, name=None):
        project = Project.objects.all()
        if id:
            project = project.filter(users__username=name)
        return project


class UserCreateMutation(graphene.Mutation):
    class Arguments:
        username = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, username, first_name, last_name, email):
        user = ToDoUser(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email)
        user.save()
        return UserCreateMutation(user)


class UserUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        username = graphene.String(required=True)

    user = graphene.Field(UserType)

    @classmethod
    def mutate(cls, root, info, id, username):
        user = ToDoUser.objects.get(id=id)
        user.username = username
        user.save()
        return UserUpdateMutation(user)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()


class ToDoUpdateMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()
        text = graphene.String(required=True)

    notice = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, id, text):
        notice = ToDo.objects.get(id=id)
        notice.text = text
        notice.save()
        return UserUpdateMutation(notice)


class Mutation(graphene.ObjectType):
    create_user = UserCreateMutation.Field()
    update_user = UserUpdateMutation.Field()
    update_todo_text = ToDoUpdateMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
