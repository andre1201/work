# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_task', '0003_auto_20150930_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('title',)},
        ),
    ]
