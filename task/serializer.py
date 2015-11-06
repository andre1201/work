from rest_framework import serializers

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'text', 'date_finaly', 'finaly')

