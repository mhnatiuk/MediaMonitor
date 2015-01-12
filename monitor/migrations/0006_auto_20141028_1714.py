# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0005_auto_20141028_1714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='position',
            field=models.IntegerField(null=True),
        ),
    ]
