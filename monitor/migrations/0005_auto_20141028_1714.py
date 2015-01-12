# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_link_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='position',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
