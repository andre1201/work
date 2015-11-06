import os
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from secretary import Renderer
from .models import Task
from restAuth import settings
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

class MixinReport():
    engine = Renderer()
    template_name = '' #name template for renders
    context = {} #data for render in template

    #renderers
    def renders(self):
        template =  os.path.join(settings.BASE_DIR, 'static', self.template_name)
        result = self.engine.render(template, **self.context)
        return result

    #return finaly report
    def get_report(self):
        response = HttpResponse(content_type='application/odt',content=self.renders())
        response['Content-Disposition'] = 'attachment; filename="renders.odt"'
        return response