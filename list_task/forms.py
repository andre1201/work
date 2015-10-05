# -*- coding: utf-8 -*-
from django import forms
from list_task.models import Task


class FTaskUpdate(forms.Form):
    title = forms.CharField();#
    text = forms.Textarea();
    term = forms.DateField();
    dateFinaly = forms.DateField();
    finaly = forms.BooleanField();
    checkDelete = forms.BooleanField();
    checkDelete.label='Поменить на удаление'
    finaly.label='Выполнено '
    dateFinaly.label='Дата выполнения задачи'
    term.label='Срок выполнения задачи'
    text.label='Tекст задачи'
    title.label='Заголовок задачи'

