# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.ManyToManyField(null=True, to='spending.Category', blank=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='tag',
            field=models.ManyToManyField(null=True, to='spending.Tag', blank=True),
        ),
    ]
