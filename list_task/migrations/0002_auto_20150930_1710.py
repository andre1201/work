# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('list_task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='dateFinaly',
            field=models.DateField(verbose_name=b'\xd0\x94\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb2\xd1\x8b\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xb4\xd0\xb0\xd1\x87\xd0\xb8'),
        ),
    ]
