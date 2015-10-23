# -*- coding: utf-8 -*-
from rest_framework import generics
from rest_framework.response import Response

from users.mixin import UserMixin


class UserList(UserMixin,generics.ListCreateAPIView):
    pass

class UserDetail(UserMixin,generics.RetrieveUpdateDestroyAPIView):

    def delete(self, request, *args, **kwargs):
        if(request.user.id!= int(kwargs['pk'])):
            self.destroy(request,*args,**kwargs)
            return Response({'ok': 'You delete ',})
        return Response({'error': 'Вы не можите удалить себя!',})