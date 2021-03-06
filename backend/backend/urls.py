"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from graphene_django.views import GraphQLView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from library.views import AuthorViewSet
from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from userapp.views import ToDoUserViewSet

router = DefaultRouter()
router.register('authors', AuthorViewSet)
router.register('users', ToDoUserViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todo', ToDoModelViewSet)

schema_view_users = get_schema_view(
    openapi.Info(
        title='userapp',
        default_version='V1',
        description='schema-view-users'
    ),
    public=True,
    permission_classes=[AllowAny]
)

schema_view_todo = get_schema_view(
    openapi.Info(
        title='todoapp',
        default_version='V1',
        description='schema-view-todo'
    ),
    public=True,
    permission_classes=[AllowAny]
)


urlpatterns = [
    path('admin/', admin.site.urls),

    # для URLPathVersioning
    # re_path('^api/(?P<version>V\d)/users/$',
    #         ToDoUserViewSet.as_view({'get': 'list'})),
    # re_path('^api/users/$',
    #         ToDoUserViewSet.as_view({'get': 'list'})),

    # для NamespaceVersioning
    path('api/users/V1', include('userapp.urls', namespace='V1')),
    path('api/users/V2', include('userapp.urls', namespace='V2')),


    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('', TemplateView.as_view(template_name='index.html')),

    path(
        'swagger_users/',
        schema_view_users.with_ui(
            'swagger',
            cache_timeout=0),
        name='schema-users-swagger'),

    path(
        'redoc_users/',
        schema_view_users.with_ui(
            'redoc',
            cache_timeout=0),
        name='schema-users-redoc'),

    path(
        'swagger_todo/',
        schema_view_todo.with_ui(
            'swagger',
            cache_timeout=0),
        name='schema-todo-swagger'),

    re_path(
        r'^swagger_todos(?P<format>\.json|\.yaml)$',
        schema_view_todo.without_ui(
            cache_timeout=0),
        name='schema-todo-json/yaml'),
]
