# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('description', models.TextField(blank=True)),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('amount', models.DecimalField(max_digits=14, decimal_places=2)),
                ('notes', models.TextField()),
                ('type', models.CharField(choices=[('Pur', 'Purchase'), ('Iou', 'Debt'), ('Uom', 'Credits')], blank=True, max_length=6)),
                ('category', models.ManyToManyField(to='spending.Category', blank=True)),
                ('tag', models.ManyToManyField(to='spending.Tag', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
