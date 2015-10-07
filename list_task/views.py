from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from list_task.models import Task, Users
from list_task.serializers import TaskSerializer,UserSerializer



@api_view(['GET', 'POST'])
def task_list(request):
    if request.method == 'GET':
        task = Task.objects.all()
        if task.exists():
            serializer = TaskSerializer(task, many=True)
            return Response(serializer.data)
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def task_detail(request,id_task):
    try:
        task = Task.objects.get(pk=id_task)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method=='GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method=='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=='PUT':
        serializer= TaskSerializer(task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def user_list(request):
    if request.method=='GET':
        user = Users.objects.all()
        if user.exists():
            serializer = UserSerializer(user,many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','DELETE','PUT'])
def user_detail(request,id_user):
    try:
        user = Users.objects.get(pk=id_user)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)

    if request.method=='GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = UserSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def task_date(request,date):
    if request.method=='GET':
        task = Task.objects.filter(term__contains=date)
        if task.exists():
            serializer = TaskSerializer(task,many=True)
            return Response(serializer.data)
    return  Response(status=status.HTTP_204_NO_CONTENT)
