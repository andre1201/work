from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from task import views

urlpatterns = [
    url(r'^$', views.api_root, name = 'Route'),
    url(r'^list/$', views.ListTask.as_view() , name = 'ListTask'),
    url(r'^(?P<pk>\d+)/$', views.DetailTask.as_view() , name = 'DetailTask'),
    url(r'^filter/$', views.FilterTask.as_view() , name = 'FilterTask'),
    url(r'^user/$', views.ListUser.as_view() , name = 'ListUser'),
    url(r'^user/(?P<pk>\d+)/$', views.DetailUser.as_view() , name = 'DetailUser'),
    url(r'^view/$', views.TaskListByUser.as_view() , name = 'TaskListByUser'),
    url(r'^view/(?P<pk>\d+)$', views.TaskDetailByUser.as_view() , name = 'TaskDetailByUser'),

]
urlpatterns = format_suffix_patterns(urlpatterns)



