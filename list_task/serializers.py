# -*- coding: utf-8 -*-
from rest_framework import  serializers
from list_task.models import Users, Task


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task






