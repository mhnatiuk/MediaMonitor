# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0003_auto_20141028_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='position',
            field=models.IntegerField(default=None, blank=True),
            preserve_default=True,
        ),
    ]
