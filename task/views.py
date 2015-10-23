# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse

from users.serializer import UserSerializer
from task.models import Task
from task.serializer import TaskSerializer


#Поиск задач
class FilterTask(generics.ListCreateAPIView):
    queryset = Task.objects.all()

    def get_queryset(self):
        if (self.request.user.is_staff != True):
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    serializer_class = TaskSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('title', 'date_finaly')


class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        #Распоковываю массив значений хранящийся в запросе к серверу

        if(request.user.id!= int(kwargs['pk'])):
            #Вызыв функции удаления, передаю параметры запроса
            self.destroy(request,*args,**kwargs)
            return Response({'ok': 'You delete ',})
        return Response({'error': 'Вы не можите удалить себя!',})


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TaskSerializer

    def get_queryset(self):
        if(self.request.user.is_staff == True):
            return Task.objects.all()
        elif (self.request.user):
            return Task.objects.filter(user=self.request.user)



#@permission_classes(IsAdminUser)
class TaskListAdmin(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        if (self.request.user.is_staff != True):
            return Task.objects.filter(user=self.request.user)
        else:
            return Task.objects.all()


class TestView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def initial(self, request, *args, **kwargs):
        if request.method == 'put' and not request.user.is_staff:
            raise PermissionDenied
        return super(TestView, self).initial( request, *args, **kwargs)





@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'task': reverse('TaskListAdmin', request=request, format=format),
    })





