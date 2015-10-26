from django.conf.urls import include, url
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = ('id', 'user', 'title', 'text', 'date_finaly', 'finaly')


class TaskSerializerAll(serializers.ModelSerializer):

    class Meta:
        model = Task


class UserPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('password')
        password = serializers.CharField(write_only=True, required=False)
        new_password = serializers.CharField(write_only=True, required=False)


    def create(self, validation_data):
        return User.objects.create(**validation_data)


    def update(self, instance, validated_data):
        password = validated_data.get('password', None)

        new_password = validated_data.get('new_password', None)
        if password and new_password and password != new_password:
            instance.set_password(new_password)
            instance.save()
            update_session_auth_hash(self.context.get('request'), instance)
            return instance
