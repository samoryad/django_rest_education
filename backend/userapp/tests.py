from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APIRequestFactory

from userapp.models import ToDoUser
from userapp.views import ToDoUserViewSet


class UserTestCase(TestCase):

    def test_get_list(self):
        # HTTP_200_OK работает для DjangoModelPermissionsOrAnonReadOnly
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = ToDoUserViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_users_list(self):
        ToDoUser.objects.create_superuser(
            'Django', 'django@gb.ru', 'geekbrains')
        ToDoUser.objects.create_user(
            username='Gogi',
            first_name='Gogi',
            last_name='Potikyan',
            email='gogi@local.com')
        client = APIClient()
        client.login(username='Django', password='geekbrains')
        response = client.get('/api/users/')
        # print(response.data['results'][1]['last_name'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        user = ToDoUser.objects.get(last_name=response.data['results'][1]['last_name'])
        # print(user)
        self.assertEqual(user.last_name, 'Potikyan')
        client.logout()
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_post_user(self):
        ToDoUser.objects.create_superuser(
            'Django', 'django@gb.ru', 'geekbrains')
        client = APIClient()
        client.login(username='Django', password='geekbrains')
        response = client.post('/api/users/',
                               {'username': 'Gogi1',
                                'first_name': 'Gogi1',
                                'last_name': 'Potikyan1',
                                'email': 'gogi1@local.com'})
        # во view пользователя нельзя создавать юзера
        self.assertEqual(
            response.status_code,
            status.HTTP_405_METHOD_NOT_ALLOWED)

