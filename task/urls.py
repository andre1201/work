from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from task import views

urlpatterns = [
    url(r'^$', views.api_root, name = 'Route'),
    url(r'^filter/$', views.FilterTask.as_view() , name = 'FilterTask'),
    url(r'^user/(?P<pk>\d+)/$', views.DetailUser.as_view() , name = 'DetailUser'),
    url(r'^list/$', views.TaskList.as_view() , name = 'TaskList'),
    url(r'^list/(?P<pk>\d+)$', views.TaskDetail.as_view() , name = 'TaskDetail'),
    url(r'^test/(?P<pk>\d+)$', views.TestView.as_view() , name = 'Test'),

]
urlpatterns = format_suffix_patterns(urlpatterns)



