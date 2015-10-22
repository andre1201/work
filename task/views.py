# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import renderers
from rest_framework import generics
from rest_framework import filters
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.reverse import reverse
from restAuth.serializer import UserSerializer
from task.models import Task

from task.serializer import TaskSerializer


class ListTask(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                  IsOwnerOrReadOnly,)
    #permission_classes = (IsOwnerOrReadOnly,)


class FilterTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'date_finaly')

class ListUser(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    #переопределяю метод
    def delete(self, request, *args, **kwargs):
        #Распоковываю массив значений хранящийся в запросе к серверу
        if(request.user!=self.queryset.get(*args,**kwargs)):
            #Вызыв функции удаления, передаю параметры запроса
            username = self.queryset.get(*args,**kwargs).username
           # self.destroy(request,*args,**kwargs)
            return Response({'ok': 'You delete user - {0} '.format(username),})
            #Просмотр значений и ключей return Response(kwargs)
        #return Response(unicode(self.queryset.get(*args,**kwargs)))
        #Можно обращаться к полям return Response(self.request.user.username)
        return Response({'error': 'Вы не можите удалить себя!',})

"""
class TaskListByUser(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        task = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(task,many=True)
        return Response(serializer.data)"""

class TaskListByUser(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

class TaskDetailByUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer
    test = 'ddf';
    test = 'ddf';
    test = 'ddf';
    def get_queryset(self):
        if (self.request.user):
            return Task.objects.filter(user=self.request.user)
        else:
            return Response({'error':'Вы не авторизированы'})


@api_view(('GET',))
def api_root(request, format=None):

    return Response({
        'task': reverse('ListTask', request=request, format=format),
        'task - user': reverse('ListUser', request=request, format=format),
        'user': reverse('ListUser', request=request, format=format),
    })





