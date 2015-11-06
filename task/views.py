# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.views.generic import View
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from restAuth import settings
from django.http import HttpResponse
from task.mixin import MixinTask, MixinTaskAdmin, MixinReport
from secretary import Renderer



#Поиск задач
from task.models import Task


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


class ReportTaskList(APIView,MixinReport):
    permission_classes = (IsAuthenticated,)
    def get(self,request):
        self.template_name = 'template-List-Task.odt'
        self.context = {
            'taskList':Task.objects.filter(user=request.user),
            'DOC_NAME':'Reropt',
        }
        return self.get_report()


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'task': reverse('TaskList', request=request, format=format),
    })





