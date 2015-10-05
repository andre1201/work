# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\x97\xd0\xb0\xd0\xb3\xd0\xbe\xd0\xbb\xd0\xbe\xd0\xb2\xd0\xbe\xd0\xba \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8')),
                ('text', models.TextField(verbose_name=b'\xd0\x9e\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8')),
                ('term', models.DateField(verbose_name=b'\xd1\x81\xd1\x80\xd0\xbe\xd0\xba \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8')),
                ('dateFinaly', models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8', blank=True)),
                ('finaly', models.BooleanField(default=False, verbose_name=b'\xd0\x92\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xbe')),
                ('checkDelete', models.BooleanField(default=False, verbose_name=b'\xd0\x9f\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x82\xd0\xb8\xd1\x82\xd1\x8c \xd0\xbd\xd0\xb0 \xd1\x83\xd0\xb4\xd0\xb0\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
            ],
            options={
                'ordering': ('idUser',),
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('login', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='task',
            name='idUser',
            field=models.ForeignKey(to='list_task.Users'),
        ),
    ]
