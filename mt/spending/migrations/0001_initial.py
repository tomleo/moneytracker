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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default='', max_length=255, blank=True)),
                ('sub_category', models.ForeignKey(blank=True, to='spending.Category', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'date taken')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('categories', models.ManyToManyField(to='spending.Category')),
                ('notes', models.ManyToManyField(to='spending.Note')),
            ],
        ),
        migrations.CreateModel(
            name='Spending',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(verbose_name=b'date published')),
                ('amount', models.DecimalField(max_digits=19, decimal_places=4)),
                ('description', models.TextField(default='', blank=True)),
                ('receipt', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('receipt_text', models.TextField(default='', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='spent',
            field=models.ForeignKey(to='spending.Spending'),
        ),
    ]
