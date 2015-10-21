from django.contrib.auth.models import User
from rest_framework import serializers
from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    class Meta:
        model = Task
        fields=('id','user','title','text','date_finaly','finaly')

class UserSerializer(serializers.ModelSerializer):
    #task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())
    class Meta:
        model = User
        fields = ('id', 'username','first_name','last_name','email','user_permissions')
