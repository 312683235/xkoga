# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0003_auto_20171130_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='add_time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='创建时间'),
        ),
    ]
