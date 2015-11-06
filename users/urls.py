from django.conf.urls import url
from users.views import UserList,UserDetail,UserUpdatePassword






urlpatterns = [
    url(r'^$', UserList.as_view(),name='user-list'),
    url(r'^(?P<pk>\d+)/$', UserDetail.as_view() , name = 'DetailUser'),
    url(r'^update/(?P<pk>\d+)/$', UserUpdatePassword.as_view() , name = 'UserUpdatePassword'),
]