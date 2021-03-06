# -*- coding: utf-8 -*-
import unittest

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from .models import Task
from django.contrib.auth.models import User
from task.serializer import TaskSerializer


#
# руализация на APITestCase
#

class TaskTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        super(TaskTestCase, cls).setUpClass()
        cls.user = User.objects.create_user('Andre', 'asdasd@sd.re', 123123)
        cls.task = Task(title='title task', text='text', date_finaly=None, user=cls.user)
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
        data = {
            "title": "title",
            "text": "teeeext",
        }
        response = self.client.post(reverse('TaskList'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_list(self):
        response = self.client.get(reverse('TaskList'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        response_detail = self.client.get(reverse('TaskDetail', args=[self.task.id]), format='json')
        self.assertEqual(response_detail.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = TaskSerializer(self.task).data
        data.update({
            "title": "test",
            "text": "text test",
        })
        response = self.client.put(reverse('TaskDetail', args=[self.task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        data = TaskSerializer(self.task).data
        response = self.client.delete(reverse('TaskDetail', args=[self.task.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


#
# руализация на unittest.TestCase
#
class TasksTestCaseUnit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TasksTestCaseUnit, cls).setUpClass()
        cls.client = APIClient()
        cls.user = User.objects.create_superuser('Andre', 'asdasd@sd.re', 123123)
        cls.task = Task(title='title task', text='text', date_finaly=None, user=cls.user)
        cls.task2 = Task(title='title task', text='text', date_finaly=None, user=cls.user)
        cls.task.save()
        cls.task2.save()
        cls.client.force_authenticate(user=cls.user)

    @classmethod
    def tearDownClass(cls):
        super(TasksTestCaseUnit, cls).tearDownClass()
        cls.user.delete()
        cls.task.delete()
        cls.task2.delete()

    def setUp(self):
        super(TasksTestCaseUnit, self).setUp()

    def test_create_task(self):
        data = {
            "title": "title",
            "text": "teeeext",
        }
        response = self.client.post(reverse('TaskList'), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_task_list(self):
        response = self.client.get(reverse('TaskList'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_task_detail(self):
        response_detail = self.client.get(reverse('TaskDetail', args=[self.task.id]), format='json')
        self.assertEqual(response_detail.status_code, status.HTTP_200_OK)

    def test_update_task(self):
        data = TaskSerializer(self.task).data
        data.update({
            "title": "test",
            "text": "text test",
        })
        response = self.client.put(reverse('TaskDetail', args=[self.task.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_task(self):
        data = TaskSerializer(self.task2).data
        response = self.client.delete(reverse('TaskDetail', args=[self.task2.id]), data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
