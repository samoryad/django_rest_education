from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory, APITestCase, \
    force_authenticate, APISimpleTestCase

from todoapp.models import ToDo
from userapp.models import ToDoUser
from userapp.views import ToDoUserViewSet


class MixerTestCase(APITestCase):

    def setUp(self):
        # код в сетап создаётся для всех тестов класса
        self.admin = ToDoUser.objects.create_superuser(
            'Django', 'django@gb.ru', 'geekbrains')
        self.client.login(username='Django', password='geekbrains')

    def test_mixer(self):
        user = mixer.blend(ToDoUser, first_name='Gogi')
        print(user)
        todo_notice = mixer.blend(ToDo, user__first_name='Gogi')
        print(todo_notice)
        todo_user = ToDoUser.objects.get(id=todo_notice.user.id)
        print(todo_user.first_name)
        response = self.client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# APITestCase создаёт клиента автоматически (client = APIClient())
class UserTestCase(APITestCase):
    """тесты для Юзера"""

    def setUp(self):
        # код в сетап создаётся для всех тестов класса
        self.admin = ToDoUser.objects.create_superuser(
            'Django', 'django@gb.ru', 'geekbrains')
        self.client.login(username='Django', password='geekbrains')

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = ToDoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        # пользователь не авторизован
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        # request = factory.get('/api/users/')
        force_authenticate(request, self.admin)
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_users_list(self):

        ToDoUser.objects.create_user(
            username='Gogi',
            first_name='Gogi',
            last_name='Potikyan',
            email='gogi@local.com')

        response = self.client.get('/api/users/')
        # print(response.data['results'][1]['last_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        user = ToDoUser.objects.get(last_name=response.data['results'][1]['last_name'])
        # print(user)
        self.assertEqual(user.last_name, 'Potikyan')
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_user(self):
        # self.client.login(username='Django', password='geekbrains')
        response = self.client.post('/api/users/',
                               {'username': 'Gogi1',
                                'first_name': 'Gogi1',
                                'last_name': 'Potikyan1',
                                'email': 'gogi1@local.com'})
        # во view пользователя нельзя создавать юзера
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED)


class FuncTest(APISimpleTestCase):
    # тестирование без разворачивания базы данных и миграций
    def func_test(self):
        self.assertTrue(True)
