# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=50)
    text = models.TextField()
    date_finaly = models.DateTimeField(null=True)
    finaly = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('title',)
