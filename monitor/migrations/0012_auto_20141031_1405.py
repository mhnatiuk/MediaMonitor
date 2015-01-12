# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0011_auto_20141031_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='link_type',
            field=models.CharField(db_index=True, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='title',
            field=models.CharField(db_index=True, max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='link',
            name='updated_time',
            field=models.DateTimeField(db_index=True, null=True, blank=True),
        ),
    ]
