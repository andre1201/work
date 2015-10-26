# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Task
from django.contrib.auth.models import User
from users.serializer import UserSerializer
from rest_framework import request
from task.serializer import TaskSerializer

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
        url_list = reverse('TaskList')
        task = Task(pk=1,title = 'title',text = 'text',date_finaly = '2015-10-16T23:21:00+03:00',user = self.user)
        task.save()
        url_detail = reverse('TaskDetail',args=[task.id])
        response = self.client.get(url_list,  format='json')
        response_detail = self.client.get(url_detail,  format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(response_detail.status_code,status.HTTP_200_OK)
        task.delete()

    def test_update_task(self):
        task = Task(pk=1,title = 'title task',text = 'text',date_finaly = '2015-10-16T23:21:00+03:00',user = self.user)
        task.save()
        data = TaskSerializer(task).data
        data.update = {
            "title": "test",
            "text": "text test",
        }
        url_detail = reverse('TaskDetail',args=[task.id])
        response = self.client.put(url_detail ,data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)
        self.assertEqual(task.title,'test')
        self.assertEqual(task.text,'text test')

    def test_delete_task(self):
        task = Task(pk=2,title = 'title task',text = 'text',date_finaly = '2015-10-16T23:21:00+03:00',user = self.user)
        task.save()
        data = TaskSerializer(task).data
        url_detail = reverse('TaskDetail',args=[task.id])
        response = self.client.delete(url_detail,data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)





