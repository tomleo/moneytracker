# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='sub_category',
        ),
        migrations.RemoveField(
            model_name='place',
            name='spent',
        ),
        migrations.AddField(
            model_name='place',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='spending',
            name='place',
            field=models.ForeignKey(blank=True, to='spending.Place', null=True),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(default='', blank=True),
        ),
    ]
