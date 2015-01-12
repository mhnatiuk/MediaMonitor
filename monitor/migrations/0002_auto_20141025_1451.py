# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='fb_shares',
        ),
        migrations.RemoveField(
            model_name='link',
            name='twitter_shares',
        ),
        migrations.AddField(
            model_name='link',
            name='stats',
            field=models.TextField(default={}),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='link',
            name='domain',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='Domain',
        ),
    ]
