from rest_framework.permissions import IsAuthenticated,IsAdminUser
from .models import Task
from task.serializer import TaskSerializer


class MixinTask():
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if (self.request.user):
            return Task.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class MixinTaskAdmin():
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAdminUser,)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)