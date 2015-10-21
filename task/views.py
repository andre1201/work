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

from task.models import Task
from task.permissions import MyUserPermissions
from task.serializer import TaskSerializer,UserSerializer


class ListTask(generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DetailTask(generics.RetrieveUpdateDestroyAPIView):

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
    queryset = User.objects.all()
    serializer_class = UserSerializer


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    #переопределяю метод
    def delete(self, request, *args, **kwargs):
        #Распоковываю массив значений хранящийся в запросе к серверу
        if(request.user!=self.queryset.get(*args,**kwargs)):
            #Вызыв функции удаления, передаю параметры запроса
            self.destroy(request,*args,**kwargs)
            return Response({'Все ок': 'Вы удалили себя!',})
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
    permission_classes = (MyUserPermissions,)
    serializer_class = TaskSerializer
    def get_queryset(self):
        #return Task.objects.all()
        return Task.objects.filter(user=self.request.user)

class TaskDetailByUser(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        if (self.request.user):
            return Task.objects.filter(user=self.request.user)
        else:
            return Response({'error':'Вы не авторизированы'})


@api_view(('GET',))
def api_root(request, format=None):

    return Response({
        'task': reverse('ListTask', request=request, format=format),
        'task-detail': reverse('DetailTask', request=request,kwargs={'pk':1}, format=format),
        'user': reverse('ListUser', request=request, format=format),
    })

class TaskHighlight(generics.GenericAPIView):
    queryset = Task.objects.all()
    renderer_classes = {renderers.StaticHTMLRenderer, }

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.user)

@api_view(['GET'])
@authentication_classes((SessionAuthentication, BasicAuthentication))
@permission_classes((IsAuthenticatedOrReadOnly  ,))
def getUser(request, format=None):

    content = {
        'user': unicode(request.user),  # `django.contrib.auth.User` instance.
        'auth': unicode(request.auth),  # None
    }
    return Response(content)

