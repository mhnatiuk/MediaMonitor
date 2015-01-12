# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0007_linkstats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='linkstats',
            name='link',
            field=models.ForeignKey(to='monitor.Link'),
        ),
    ]
