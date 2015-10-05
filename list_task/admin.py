# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Users,Task

admin.site.register(Task)
admin.site.register(Users)