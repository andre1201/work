# -*- coding: utf-8 -*-
from django.conf.urls import  url
from list_task import views




urlpatterns = [
    url(r'^$', views.task_list , name = 'task_list'),
    url(r'^(?P<id_task>\d+)/$', views.task_detail , name = 'task_detail'),
    url(r'^(?P<date>((\d{4}-\d{2}-\d{2})||(\d{2}:\d{0,2}))||(\d{4}-\d{2}-\d{2} \d{2}:\d{0,2}))/$', views.task_date , name = 'task_date'),
    url(r'^user/$', views.user_list , name = 'user_list'),
    url(r'^user/(?P<id_user>\d+)/$', views.user_detail , name = 'user_detail'),
    url(r'^tasklist/$', views.TasksList.as_view() , name = 't_list_generic'),
]