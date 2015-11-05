# -*- coding: utf-8 -*-
import unittest
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from users.serializer import UserSerializer
from rest_framework import request
from task.serializer import TaskSerializer

#
# руализация на APITestCase
#

class UserTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(UserTestCase, cls).setUpClass()
        cls.user = User.objects.create_user('Andre','asdasd@sd.re',123123)


    @classmethod
    def tearDownClass(cls):
        super(UserTestCase, cls).tearDownClass()
        cls.user.delete()



    def setUp(self):
        super(UserTestCase, self).setUp()
        self.client.force_authenticate(self.user)


    def test_create_user(self):
        data = {
            "username": "Vasa",
            "email": "sdasd@mail.ru",
            "is_staff": False
        }
        response = self.client.post(reverse('user-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_get_user_list(self):
        response = self.client.get(reverse('user-list'),  format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_user_detail(self):
        response_detail = self.client.get(reverse('DetailUser',args=[self.user.id]),  format='json')
        self.assertEqual(response_detail.status_code,status.HTTP_200_OK)


    def test_update_user(self):
        data = UserSerializer(self.user).data
        data.update ( {
            "username": "test",
        })
        response = self.client.put(reverse('DetailUser', args=[self.user.id]), data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_user_self(self):
        data = UserSerializer(self.user).data
        response = self.client.delete(reverse('DetailUser',args=[self.user.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_user_other(self):
        test_user = User.objects.create_user('Test','asdasd@sd.re',1213123)
        data = UserSerializer(test_user).data
        response = self.client.delete(reverse('DetailUser',args=[test_user.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


#
# руализация на unittest.TestCase
#
class UserTestCaseUnittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        super(UserTestCaseUnittest, cls).setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_user('Andre','asdasd@sd.re',123123)


    @classmethod
    def tearDownClass(cls):
        super(UserTestCaseUnittest, cls).tearDownClass()
        cls.user.delete()



    def setUp(self):
        super(UserTestCaseUnittest, self).setUp()
        self.client.force_authenticate(self.user)


    def test_create_user(self):
        data = {
            "username": "Vasa",
            "email": "sdasd@mail.ru",
            "is_staff": False
        }
        response = self.client.post(reverse('user-list'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_get_user_list(self):
        response = self.client.get(reverse('user-list'),  format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_user_detail(self):
        response_detail = self.client.get(reverse('DetailUser',args=[self.user.id]),  format='json')
        self.assertEqual(response_detail.status_code,status.HTTP_200_OK)


    def test_update_user(self):
        data = UserSerializer(self.user).data
        data.update ( {
            "username": "test",
        })
        response = self.client.put(reverse('DetailUser', args=[self.user.id]), data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_user_self(self):
        data = UserSerializer(self.user).data
        response = self.client.delete(reverse('DetailUser',args=[self.user.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_200_OK)

    def test_delete_user_other(self):
        test_user = User.objects.create_user('Test','asdasd@sd.re',1213123)
        data = UserSerializer(test_user).data
        response = self.client.delete(reverse('DetailUser',args=[test_user.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)


#
# руализация на APITestCase
#ПРоверка на авторизацию
#
class UserIsAuthTestCase(APITestCase):

    @classmethod
    def setUpClass(cls):
        super(UserIsAuthTestCase, cls).setUpClass()
        cls.user = User.objects.create_user('Andre','asdasd@sd.re',123123)


    @classmethod
    def tearDownClass(cls):
        super(UserIsAuthTestCase, cls).tearDownClass()
        cls.user.delete()


    def test_get_user_list_auth(self):
        response = self.client.get(reverse('user-list'),  format='json')
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)


    def test_get_user_detail_auth(self):
        response_detail = self.client.get(reverse('DetailUser',args=[self.user.id]),  format='json')
        self.assertEqual(response_detail.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_update_user_auth(self):
        data = UserSerializer(self.user).data
        data.update ( {
            "username": "test",
        })
        response = self.client.put(reverse('DetailUser', args=[self.user.id]), data)
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

    def test_delete_user_self_auth(self):
        data = UserSerializer(self.user).data
        response = self.client.delete(reverse('DetailUser',args=[self.user.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_401_UNAUTHORIZED)

