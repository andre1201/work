# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from task.mixin import MixinTask, MixinTaskAdmin


#Поиск задач
class FilterTask(MixinTask,generics.ListCreateAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'date_finaly')

#просмотр  задачи
class TaskDetail(MixinTask,generics.RetrieveUpdateDestroyAPIView):
    pass

class TaskList(MixinTask,generics.ListCreateAPIView):
    pass

class TaskListAdmin(MixinTaskAdmin,generics.ListCreateAPIView):
    pass

class TaskDetailAdmin(MixinTaskAdmin,generics.RetrieveUpdateDestroyAPIView):
    pass

@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'task': reverse('TaskList', request=request, format=format),
    })





