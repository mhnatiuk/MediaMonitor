# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20141030_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='uri',
            field=models.CharField(unique=True, max_length=1000, db_index=True),
        ),
        migrations.AlterField(
            model_name='linkstats',
            name='link_uri',
            field=models.CharField(max_length=1000, db_index=True),
        ),
        migrations.AlterField(
            model_name='linkstats',
            name='time',
            field=models.DateTimeField(db_index=True),
        ),
    ]
