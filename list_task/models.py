# -*- coding: utf-8 -*-
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=60)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    def __str__(self):
        return self.name;
    class Meta:
        ordering = ('name',)



class Task(models.Model):
    idUser = models.ForeignKey(Users);
    title = models.CharField(max_length=200,verbose_name='Заголовок задачи');#
    text = models.TextField(verbose_name='Описание задачи');
    term = models.DateField(verbose_name='срок выполнения задачи');
    dateFinaly = models.DateField(verbose_name='Дата выполнения задачи',blank=True,null=True);
    finaly = models.BooleanField(default=False,verbose_name='Выполнено',blank=True);
    checkDelete = models.BooleanField(default=False,verbose_name='Пометить на удаление',blank=True);
    def __str__(self):
        return self.title;
    class Meta:
        ordering = ('title',)









