# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=400)),
                ('recursion_level', models.IntegerField(default=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uri', models.CharField(max_length=1000)),
                ('fb_shares', models.IntegerField(default=None)),
                ('twitter_shares', models.IntegerField(default=None)),
                ('ttl', models.DateTimeField()),
                ('domain', models.ForeignKey(to='monitor.Domain')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
