from django.conf.urls import include, url

urlpatterns = [
    url(r'^user/', include('users.urls')),
    url(r'^task/', include('task.urls')),
]
