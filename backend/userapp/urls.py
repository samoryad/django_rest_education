from django.urls import path
from userapp.views import ToDoUserViewSet

app_name = 'userapp'

urlpatterns = [
    path('', ToDoUserViewSet.as_view({'get': 'list'})),
]
