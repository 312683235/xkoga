# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 19:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0018_auto_20171217_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='he.City', verbose_name='城市'),
        ),
    ]
