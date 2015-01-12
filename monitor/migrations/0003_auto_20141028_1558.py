# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20141025_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='domain',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='stats',
            field=models.TextField(default=b'{}', blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='ttl',
            field=models.DateTimeField(default=None, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='uri',
            field=models.CharField(unique=True, max_length=1000),
        ),
    ]
