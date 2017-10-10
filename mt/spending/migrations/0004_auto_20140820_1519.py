# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spending', '0003_category_tags'),
    ]

    operations = [
        migrations.CreateModel(
            name='BudgetItem',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('amount', models.DecimalField(max_digits=14, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('timestamp',)},
        ),
        migrations.AddField(
            model_name='transaction',
            name='budget_item',
            field=models.ForeignKey(blank=True, null=True, to='spending.BudgetItem'),
            preserve_default=True,
        ),
    ]
