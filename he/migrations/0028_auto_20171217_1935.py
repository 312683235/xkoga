# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-17 19:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('he', '0027_auto_20171217_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='consultation',
            name='click_num',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='images',
        ),
        migrations.RemoveField(
            model_name='consultation',
            name='is_banner',
        ),
    ]
