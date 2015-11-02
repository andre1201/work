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

    @classmethod
    def setUpClass(cls):
        super(TaskTestCase, cls).setUpClass()
        cls.user = User.objects.create_user('Andre','asdasd@sd.re',123123)
        cls.task = Task(pk=2,title = 'title task',text = 'text',date_finaly = None,user = cls.user)
        cls.task.save()


    @classmethod
    def tearDownClass(cls):
        super(TaskTestCase, cls).tearDownClass()
        cls.user.delete()
        cls.task.delete()


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
        self.assertEqual(Task.objects.get(pk=1).title, 'title')


    def test_get_task_list(self):
        response = self.client.get(reverse('TaskList'),  format='json')
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_get_task_detail(self):
        response_detail = self.client.get(reverse('TaskDetail',args=[self.task.id]),  format='json')
        self.assertEqual(response_detail.status_code,status.HTTP_200_OK)


    def test_update_task(self):
        data = TaskSerializer(self.task).data
        data.update ( {
            "title": "test",
            "text": "text test",
        })
        response = self.client.put(reverse('TaskDetail', args=[self.task.id]), data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


    def test_delete_task(self):
        data = TaskSerializer(self.task).data
        response = self.client.delete(reverse('TaskDetail',args=[self.task.id]),data, format='json' )
        self.assertEqual(response.status_code,status.HTTP_204_NO_CONTENT)





