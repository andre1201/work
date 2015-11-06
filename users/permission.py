from rest_framework.permissions import BasePermission
from django.contrib.auth.models import User

class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
       # if (request.user and not request.user.is_staff):
       #     return request.user and not request.user.is_staff
        return request.user and request.user.is_staff