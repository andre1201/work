from django.conf.urls import url, patterns, include
from rest_framework.routers import DefaultRouter

from task import views


urlpatterns = [
    url(r'^$', views.api_root, name = 'Route'),
    url(r'^test/(?P<pk>[0-9]+)/user/$', views.TaskHighlight.as_view()),
    url(r'^list/$', views.ListTask.as_view() , name = 'ListTask'),
    url(r'^(?P<pk>\d+)/$', views.DetailTask.as_view() , name = 'DetailTask'),
    url(r'^filter/$', views.FilterTask.as_view() , name = 'FilterTask'),
    url(r'^user/$', views.ListUser.as_view() , name = 'ListUser'),
    url(r'^user/(?P<pk>\d+)/$', views.DetailUser.as_view() , name = 'DetailUser'),
    url(r'^view/$', views.TaskListByUser.as_view() , name = 'TaskListByUser'),
    url(r'^view/(?P<pk>\d+)$', views.TaskDetailByUser.as_view() , name = 'TaskDetailByUser'),
    url(r'^ex/$', views.getUser , name = 'example_view'),
]

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)

