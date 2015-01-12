# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0010_auto_20141031_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='link_type',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='title',
            field=models.CharField(max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='link',
            name='updated_time',
            field=models.DateTimeField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
