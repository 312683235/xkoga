# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-30 18:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0002_auto_20171130_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='public',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
    ]