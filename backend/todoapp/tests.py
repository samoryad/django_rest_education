from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase, \
    force_authenticate

from todoapp.models import Project, ToDo
from todoapp.views import ToDoModelViewSet
from userapp.models import ToDoUser


class TodoTestCase(APITestCase):
    """тесты для заметок"""

    def setUp(self):
        # Создаём юзера и логиним для всех тестов класса
        self.admin = ToDoUser.objects.create_superuser(
            'Django', 'django@gb.ru', 'geekbrains')
        self.client.login(username='Django', password='geekbrains')

    def test_get_todo_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/todo/')
        view = ToDoModelViewSet.as_view({'get': 'list'})
        response = view(request)
        # пользователь не авторизован
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # авторизуемся
        force_authenticate(request, self.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_projects_list(self):

        Project.objects.create(
            name='project1',
            link='project1.local')

        response = self.client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project = Project.objects.get(name=response.data['results'][0]['name'])
        self.assertEqual(project.name, 'project1')
        self.client.logout()
        response = self.client.get('/api/project/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_todo_list(self):
        todo = mixer.blend(ToDo)
        response = self.client.get(f'/api/users/{todo.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_todo(self):
        Project.objects.create(
            name='project1',
            link='project1.local')

        response = self.client.post('/api/todo/',
                                    {'project': 'project1',
                                     'text': 'npiqjervfhbp9uoiasfv',
                                     'created_date': 12345,
                                     'updated_date': 12334,
                                     'user': 1})
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED)
