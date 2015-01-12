# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0006_auto_20141028_1714'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkStats',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('link_uri', models.CharField(max_length=1000)),
                ('time', models.DateTimeField()),
                ('fb_21', models.TextField()),
                ('fb_rest', models.TextField()),
                ('twitter', models.TextField()),
                ('link', models.OneToOneField(to='monitor.Link')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
