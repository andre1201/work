from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from task import views

urlpatterns = [
    url(r'^$', views.api_root, name='Route'),
    url(r'^filter/$', views.FilterTask.as_view(), name='FilterTask'),
    url(r'^list/$', views.TaskList.as_view(), name='TaskList'),
    url(r'^list/(?P<pk>\d+)$', views.TaskDetail.as_view(), name='TaskDetail'),
    url(r'^admin/$', views.TaskListAdmin.as_view(), name='TaskListAdmin'),
    url(r'^admin/(?P<pk>\d+)$', views.TaskDetailAdmin.as_view(), name='TaskDetailAdmin'),
    url(r'^list/report/$', views.ReportTaskList.as_view(), name='Report'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
