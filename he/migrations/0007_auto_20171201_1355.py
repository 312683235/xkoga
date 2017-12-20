# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-01 13:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0006_remove_public_add_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='public',
            name='add_time',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='public',
            name='run_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='产品上线时间'),
        ),
    ]
