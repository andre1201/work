# coding=utf-8
from __future__ import unicode_literals
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view, list_route

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.views import APIView

from task.mixin import MixinTask, MixinTaskAdmin
from task.commons.MixinReport import MixinReport
from task.models import Task
from task.serializer import TaskSerializer

class FilterTask(MixinTask, generics.ListCreateAPIView):
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'date_finaly')


# просмотр  задачи
class TaskDetail(MixinTask, generics.RetrieveUpdateDestroyAPIView):
    pass


class TaskList(MixinTask, generics.ListCreateAPIView):
    pass


class TaskListAdmin(MixinTaskAdmin, generics.ListCreateAPIView):
    pass


class TaskDetailAdmin(MixinTaskAdmin, generics.RetrieveUpdateDestroyAPIView):
    pass


class TaskViewSet(viewsets.ModelViewSet):

    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)





class ReportTaskList(APIView, MixinReport):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        self.template_name = 'template-List-Task.odt'
        self.context = {
            'taskList': Task.objects.filter(user=request.user),
            'DOC_NAME': 'Reropt',
        }
        return self.get_report()


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'task': reverse('TaskList', request=request, format=format),
    })


