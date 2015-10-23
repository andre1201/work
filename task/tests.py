# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task
from django.contrib.auth.models import User
from users.serializer import UserSerializer
from rest_framework import request

class TaskTestCase(APITestCase):

    #инициализирует класс один раз в самом начале
    @classmethod
    def setUpClass(cls):
        super(TaskTestCase, cls).setUpClass()
        cls.user = User.objects.create_user('Andre','asdasd@sd.re',123123)

    # удалает после себя данные после завершения теста
    @classmethod
    def tearDownClass(cls):
        super(TaskTestCase, cls).tearDownClass()
        cls.user.delete()

    #Выполняется перед каждым методом теста
    def setUp(self):
        super(TaskTestCase, self).setUp()
        self.client.force_authenticate(self.user)

    def test_create_task(self):

        url = reverse('TaskList')
        data = {
            "title": "title",
            "text": "teeeext"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'title')

    def test_get_task(self):
        task = Task.objects.create('title','text','none','none',user)
        serializer = UserSerializer(user)
        request.user = serializer.data
        response = self.client.get(url, data, format='json')


