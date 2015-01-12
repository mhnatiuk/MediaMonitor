# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20141028_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 30, 21, 10, 18, 578040), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='link',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 30, 21, 10, 33, 93980), auto_now=True),
            preserve_default=False,
        ),
    ]
